#!/bin/bash

#SBATCH --job-name=qmc
#SBATCH --account=rc-ma1200
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --time=00:30:00
#SBATCH --error=10.err
#SBATCH --output=10.out
#SBATCH --partition=batch-all

# Input arguments to this script, in order: J, delta, j_scaling

source /beegfs/scratch/user/s/orp20/own-utilities/helmholtz_firedrake_venv.sh

M=`python running_helmholtz_monte_carlo/calculate_m.py 10.0`

pcprop=`python calculate_nbpc_rate.py 10.0`

mpirun -n 16 python /beegfs/scratch/user/s/orp20/running-helmholtz-monte-carlo/investigate_convergence.py 10.0 1 ${M} 1 $1 $2 1.0 $3 2 1 1.0 -1.5 1 ${pcprop} 'integral' 'origin' 'top_right' 'gradient_top_right'
