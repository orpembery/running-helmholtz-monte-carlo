#!/bin/bash

for k in 10 20 30 40 50 60
do
    sbatch jobscript-k.slurm ${k}
done