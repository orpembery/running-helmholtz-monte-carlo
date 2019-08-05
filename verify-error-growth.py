import numpy as np
from matplotlib import pyplot as plt
from calculate_m import calc_M

k = np.array([10,20,30,40,50,60])#np.arange(10.0,60.0)

# These values are for point evaluation at the origin now in base e logs

C = 6.5 * 10.0**(-3)

alpha0 = 1.35

alpha1 = 0.17

CN = np.log(2048.0) * (alpha0 - alpha1*np.log(10.0))

print(CN)

alpha = alpha0 - alpha1*np.log(k)

for N in [np.exp(CN / alpha),2.0**np.array([calc_M(this_k) for this_k in k])]:

    print(-CN * alpha)

    print(np.log2(N))

    Err = C * N**-alpha

    plt.semilogy(k,N,basey=2.0)
    plt.xlabel('$k$')
    plt.ylabel('$N$')
    plt.show()

    plt.plot(k,Err)

    plt.xlabel('$k$')

    plt.ylabel('Projected QMC error')

    plt.title(r'Projected QMC error')

    plt.show()
