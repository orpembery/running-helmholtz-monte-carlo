import numpy as np
from matplotlib import pyplot as plt
import sys

k = float(sys.argv[1])

k_list = np.array([10.0,20.0,30.0])

prop  = [0.24,0.48,0.78]

#plt.plot(k_list,prop,'o')

fit = np.polyfit(k_list,prop,deg=1)

# Polyfit uses (in my opinion) the wrong notational convention
fit_0 = fit[1]

fit_1 = fit[0]

#print(fit_0,fit_1)

#plt.plot(k,fit_0 + fit_1*k,'--')

#plt.show()

# The above figures were percentages, but we need a proportion

print((fit_0 + fit_1*k)/100.0)
   
