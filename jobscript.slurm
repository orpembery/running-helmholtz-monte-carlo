#!/bin/bash

#SBATCH --job-name=qmc
#SBATCH --account=rc-ma1200
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=16
#SBATCH --time=00:10:00
#SBATCH --error=%j.err
#SBATCH --output=%j.out
#SBATCH --partition=batch-all

source /beegfs/scratch/user/s/orp20/own-utilities/helmholtz_firedrake_venv.sh

mpirun -n 32 python /beegfs/scratch/user/s/orp20/running-helmholtz-monte-carlo/checking_convergence.py 50.0 0 11 20