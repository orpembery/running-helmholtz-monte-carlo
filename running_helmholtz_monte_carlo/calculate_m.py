import numpy as np
import sys

def alpha(k):
    # These values of alpha were determined from experimental data
    return 1.38 - 0.19 * np.log(k)

def calc_M(k):
    # Based on experimental data, we want N to scale like
    # exp(D\alpha^{-1}).


    # Experimental data was gained for 2048 points. We'll do things
    # so that for k=10.0, we have 2048 points.
    D = alpha(10.0) * np.log(2048.0)

    k = float(k)

    N = np.exp(D/alpha(k))

    M = int(np.round(np.log2(N)))

    return M



if __name__ == '__main__':
    
    print(calc_M(sys.argv[1]))

