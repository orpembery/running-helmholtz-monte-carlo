#!/bin/bash

#SBATCH --job-name=qmc
#SBATCH --account=free
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=16
#SBATCH --time=00:03:00
#SBATCH --error=$1-%j.err
#SBATCH --output=$1-%j.out
#SBATCH --partition=batch-devel
#SBATCH --qos=devel

#source /beegfs/scratch/user/s/orp20/own-utilities/helmholtz_firedrake_venv.sh

#mpirun -n 32 python /beegfs/scratch/user/s/orp20/running-helmholtz-monte-carlo/checking_convergence.py 50.0 0 11 20

echo $1