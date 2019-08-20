import sys
from running_helmholtz_monte_carlo.nbpc_percentage_fit import nbpc_fit

k = float(sys.argv[1])

fits = nbpc_fit()

fit_0 = fits[0]

fit_1 = fits[1]

# The above figures were percentages, but we need a proportion

print((fit_0 + fit_1*k)/100.0)
   
