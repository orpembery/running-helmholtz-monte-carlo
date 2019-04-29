#!/bin/bash

for k in 1 2 4 8
do
python investigate_convergence.py ${k} 2 4 5 11 1.1 0.9 1.05 2 0 'integral' 'top_right' 'gradient_top_right'
done
