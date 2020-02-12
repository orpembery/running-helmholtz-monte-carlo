#!/bin/bash

# Yes, this will need to be made reproducible....

# This script was NOT used in my thesis, but was for potential computations to assess whether the QMC error is really kept bounded by scaling the QMC points as we do. These computations were not carried out in my thesis.

for J in 10
do
    for delta in 1.0
    do
	for j_scaling in 4.0
	do	    
	    echo ${J}
	    echo ${delta}
	    echo ${j_scaling}
	    sbatch jobscript10-var-points-shifts.slurm ${J} ${delta} ${j_scaling}
            sbatch jobscript20-var-points-shifts.slurm ${J} ${delta} ${j_scaling}
            sbatch jobscript30-var-points-shifts.slurm ${J} ${delta} ${j_scaling}
            #sbatch jobscript40-GMRES.slurm ${J} ${delta} ${j_scaling}
            #sbatch jobscript50-GMRES.slurm ${J} ${delta} ${j_scaling}
            #sbatch jobscript60-GMRES.slurm ${J} ${delta} ${j_scaling}
	done
    done
done
