#!/bin/bash

#SBATCH --job-name=qmc
#SBATCH --account=rc-ma1200
#SBATCH --nodes=32
#SBATCH --ntasks-per-node=16
#SBATCH --time=36:00:00
#SBATCH --error=%j.err
#SBATCH --output=%j.out
#SBATCH --partition=batch-all

source /beegfs/scratch/user/s/orp20/own-utilities/helmholtz_firedrake_venv.sh

M=`python calculate_m.py 50.0`

mpirun -n 512 python /beegfs/scratch/user/s/orp20/running-helmholtz-monte-carlo/investigate_convergence.py 50.0 1 ${M} 1 $1 $2 1.0 $3 2 1 'integral' 'origin' 'top_right' 'gradient_top_right'
