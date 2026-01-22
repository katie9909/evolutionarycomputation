This repository contains a genetic algorithm implementation for solving the 2D cylinder loading problem

Overview
The solution uses a permutaiton-based GA wih a tangent-based placement decoder to pack cylinders into containers while satisfying geometric, weight, and centre-of-mass constraints.

Requires:
Python 3.X
NumPy
Matplotlib

files:
'ga_run.py - Main GA implementation
'placement.py' - Tangent-based placement decoder
'fitness.py' - Constraint evaluation
'visualise.py' - solution visualisation
'test_ga_on_basic/challenging_instances.py' - both show fitness 0.00 result
Other files: supporting files for GA operators, instances, etc.
