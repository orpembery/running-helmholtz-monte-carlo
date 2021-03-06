from helmholtz_monte_carlo import generate_samples as gen
import pickle
import numpy as np
import sys
import firedrake as fd
from os import mkdir
import subprocess
import datetime
from helmholtz_firedrake import utils
from running_helmholtz_monte_carlo.name_writing import name_writing, make_quants
from copy import deepcopy

"""Entries are (in order) (see helmholtz_monte_carlo.generate_samples.generate_samples for an explanation):

k
number of h levels (also determines fine grid for doing QMC convergence calculations) NOTE, this is a departure from earlier syntax.
M (where number of QMC points is 2**M)
number of shifts
J
delta
lambda_mult
j_scaling
dim
on_balena
h_coarse_spec[0]
h_coarse_spec[1]
nearby_preconditioning
nearby_preconditioning_proportion

All subsequent arguments should be strings, giving the names of the qois to consider
"""
quants = make_quants(sys.argv[1:])

if quants['on_balena']:
        print('loading module')
        from firedrake_complex_hacks import balena_hacks
        balena_hacks.fix_mesh_generation_time()

# Strategy for saving the files:
# 1. Create a uniquely named folder, with name of the form: properties, hash, date/time
#2. Within this folder, save k, samples, and n_coeffs (and anything else that comes along later) in generically-named files

# Analysis script will then:
# 1. Take in the parameters we want to use for analysis (e.g., values of k, j_scaling, etc.)
#2. Find the folders corresponding to all the parameters we want (throw a question if there's more than one exact match - default is to take the newest
# Do the analysis required (probably the same plots we have at the moment, just including everything in the title)

if fd.COMM_WORLD.rank == 0:
        # Add all values to start of folder name
        quants_tmp = deepcopy(quants)

        quants_tmp['nbpc_prop'] = np.round(10.0**5.0 * quants_tmp['nbpc_prop']) / 10.0**5.0

        folder_name = name_writing(quants_tmp)

	# Get git hash
        git_hash = subprocess.run("git rev-parse HEAD", shell=True,
                                  stdout=subprocess.PIPE)

        # help from https://stackoverflow.com/a/6273618
        folder_name += '-git-hash-' + git_hash.stdout.decode('UTF-8')[:-1][:6]

	# Get current date and time
	# This initialises the object. I don't understand why this is
	# necessary.
        date_time = datetime.datetime(1,1,1)
        folder_name += '-' + date_time.utcnow().isoformat()

        folder_name += '/'

    

h_coarse_spec = (quants['h_coarse_mag'],quants['h_coarse_scal'])

for h_refinement in range(quants['num_h']):

    # First fix h and vary number of QMC points
    
    h_spec = (h_coarse_spec[0]/(2.0**h_refinement),h_coarse_spec[1])
    
    dim = quants['dim']

    k = quants['k']

    dofs = (utils.h_to_num_cells(h_spec[0]*k**h_spec[1],dim)+1)**dim

    # Assumes number of cores is a power of 2

    num_spatial_cores = int(2**np.floor(np.log2(np.max((1,dofs//50000))))) # 50,000 is Firedrake's recommendend minimum number of DoFs per node to get good parallel scalability
     
    qmc_out = gen.generate_samples(k=k,h_spec=h_spec,J=quants['J'],
                                   nu=quants['nu'],M=quants['M_high'],
                                   point_generation_method='qmc',
                                   delta=quants['delta'],
                                   lambda_mult=quants['lambda_mult'],
                                   j_scaling=quants['j_scal'],
                                   qois=quants['qois'],
                                   num_spatial_cores=num_spatial_cores,
                                   dim=dim,display_progress=True,
                                   physically_realistic=False,
                                   nearby_preconditioning=quants['nbpc'],
                                   nearby_preconditioning_proportion=quants['nbpc_prop'])
    
    if fd.COMM_WORLD.rank == 0:
        if h_refinement == 0:          
                mkdir(folder_name)

        with open('./' + folder_name + 'output-h_magnitude-' +str(h_spec[0]) + '.pickle','wb') as f:
                pickle.dump(qmc_out,f)
