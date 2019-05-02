#!/bin/bash

#SBATCH --job-name=qmc
#SBATCH --account=rc-ma1200
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=16
#SBATCH --time=24:00:00
#SBATCH --error=%j.err
#SBATCH --output=%j.out
#SBATCH --partition=batch-all

source /beegfs/scratch/user/s/orp20/own-utilities/helmholtz_firedrake_venv.sh

mpirun -n 32 python /beegfs/scratch/user/s/orp20/running-helmholtz-monte-carlo/investigate_convergence.py 40.0 1 11 20 $1 $2 1.0 $3 2 1 'integral' 'origin' 'top_right' 'gradient_top_right'