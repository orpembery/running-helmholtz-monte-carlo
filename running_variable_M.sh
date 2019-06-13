#!/bin/bash

# Yes, this will need to be made reproducible....

for J in 10 #10 20
do
    for delta in 1.0 #0.0 1.0
    do
	for j_scaling in 4.0 1.0 2.0 4.0
	do	    
	    echo ${J}
	    echo ${delta}
	    echo ${j_scaling}
	    sbatch jobscript10.slurm ${J} ${delta} ${j_scaling}
            sbatch jobscript20.slurm ${J} ${delta} ${j_scaling}
            sbatch jobscript30.slurm ${J} ${delta} ${j_scaling}
            #sbatch jobscript40.slurm ${J} ${delta} ${j_scaling}
            #sbatch jobscript50.slurm ${J} ${delta} ${j_scaling}
            #sbatch jobscript60.slurm ${J} ${delta} ${j_scaling}
	done
    done
done