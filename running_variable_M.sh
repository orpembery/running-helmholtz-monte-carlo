#!/bin/bash

# Yes, this will need to be made reproducible....

for J in 10
do
    for delta in 1.0
    do
	for j_scaling in 4.0
	do	    
	    echo ${J}
	    echo ${delta}
	    echo ${j_scaling}
	    #sbatch jobscript10-GMRES.slurm ${J} ${delta} ${j_scaling}
            sbatch jobscript20-GMRES.slurm ${J} ${delta} ${j_scaling}
            sbatch jobscript30-GMRES.slurm ${J} ${delta} ${j_scaling}
            #sbatch jobscript40-GMRES.slurm ${J} ${delta} ${j_scaling}
            #sbatch jobscript50-GMRES.slurm ${J} ${delta} ${j_scaling}
            #sbatch jobscript60-GMRES.slurm ${J} ${delta} ${j_scaling}
	done
    done
done
