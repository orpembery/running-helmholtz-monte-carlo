from helmholtz_monte_carlo import error_analysis as err
import pickle
import numpy as np

# All the parameters for assesing convergence

k_list =  [5.0]#[10.0]#,20.0,30.0]

#ppw = 10

h_coarse_spec = (1.0,-1.5)#(2.0*np.pi/ppw,-1.0)

h_refinement_levels = 2

h_fine_spec = (h_coarse_spec[0]/(2.0**h_refinement_levels),h_coarse_spec[1])

# N = #QMC points = 2**M

#M_low = 7

#M_refinement_levels = 3

M_high = 6#11#M_low + M_refinement_levels


# All the parameters for specifying the problem - leave unchanged
J = 10

nu = 20

delta = 1.0

lambda_mult = 1.0

qois = ['integral'] # Have changed here from previous versions

# Actually run the code
for k in k_list:
    # First fix h and vary number of QMC points

    h_spec = h_fine_spec

    #    for M in range(M_low,M_high+1):

    M = M_high
       
    qmc_out = err.investigate_error(k,h_spec,J,nu,M,'qmc',delta,lambda_mult,qois,dim=2,display_progress=True)

    #print(qmc_out)
    with open('k-'+str(k)+'-h-magnitude-'+str(h_spec[0])+'-M-'+str(M)+'-all-qmc-samples.pickle','wb') as f:
        pickle.dump(qmc_out,f)
        
    # Then fix number of QMC points and vary h

    # Don't need to do the finest level, because it's been done already!
    for h_refinement in range(h_refinement_levels):

        M = M_high
        
        h_spec = (h_coarse_spec[0]/(2.0**h_refinement),h_coarse_spec[1])

        qmc_out = err.investigate_error(k,h_spec,J,nu,M,'qmc',delta,lambda_mult,qois,dim=2,display_progress=True)

        #print(qmc_out)
        with open('k-'+str(k)+'-h-magnitude-'+str(h_spec[0])+'-M-'+str(M)+'-all-qmc-samples.pickle','wb') as f:
            pickle.dump(qmc_out,f)


