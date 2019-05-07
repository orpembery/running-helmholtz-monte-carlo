#!/bin/bash

mpirun -n 4 python investigate_convergence.py 20.0 1 11 20 $1 $2 1.0 $3 2 0 'integral' 'origin' 'top_right' 'gradient_top_right'
