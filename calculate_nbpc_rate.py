import sys
from running_helmholtz_monte_carlo.nbpc_percentage_fit import nbpc_fit

def make_fits():

    fits = nbpc_fit()

    fit_0 = fits[0]

    fit_1 = fits[1]

    return [fit_0,fit_1]

# The above figures were percentages, but we need a proportion

if __name__ == '__main__':

    [fit_0,fit_1] = make_fits()

    k = float(sys.argv[1])

    print((fit_0 + fit_1*k)/100.0)
   
