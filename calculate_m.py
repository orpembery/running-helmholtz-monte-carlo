import numpy as np
import sys

def calc_M(k):
    # Nicked from nbpc library

    # Based on experimental data, want N to scale like
    # k^{3.5}. Experimental data was gained for 2048 points, but that
    # takes a long time So N = D * k**3.5, and we'll do things so that
    # for k=10.0, we have 128 points.
    D = 2048/(10**3.5)
    # So M = log2(D * k^{3.5})

    k = float(k)

    M = int(np.round(np.log2(D*k**3.5)))

    return M

if __name__ == '__main__':
    print(calc_M(sys.argv[1]))
