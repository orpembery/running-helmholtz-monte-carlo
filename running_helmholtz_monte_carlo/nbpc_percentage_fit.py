import numpy as np
from matplotlib import pyplot as plt

# From the (inputted by hand) results of the sequential nbpc algorithm, compute the fit

def nbpc_fit(printing=False):

    k_list = np.array([10.0,20.0,30.0])

    prop  = [0.24,0.48,0.78]

    #plt.plot(k_list,prop,'o')

    fit = np.polyfit(k_list,prop,deg=1)

    # Polyfit uses (in my opinion) the wrong notational convention
    fit_0 = fit[1]

    fit_1 = fit[0]

    if printing:

        print(fit_0,fit_1)

    else:

        return [fit_0,fit_1]

def make_fits():

    fits = nbpc_fit()

    fit_0 = fits[0]

    fit_1 = fits[1]

    return [fit_0,fit_1]

   
if __name__ == '__main__':

    nbpc_fit(True)
