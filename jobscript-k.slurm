#!/bin/bash

#SBATCH --job-name=qmc
#SBATCH --account=rc-ma1200
#SBATCH --nodes=16
#SBATCH --ntasks-per-node=16
#SBATCH --time=16:00:00
#SBATCH --error=%j.err
#SBATCH --output=%j.out
#SBATCH --partition=batch-all

source /beegfs/scratch/user/s/orp20/own-utilities/helmholtz_firedrake_venv.sh

mpirun -n 256 python /beegfs/scratch/user/s/orp20/running-helmholtz-monte-carlo/investigate_convergence.py $1 1 11 20 10 1.0 1.0 4.0 2 1 0.002 0.0 'integral' 'origin' 'top_right' 'gradient_top_right'