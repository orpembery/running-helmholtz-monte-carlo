import numpy as np

# Figuring out number of QMC points:

D = 2048/(10.0**3.5)

N = []

for k in [10.0,20.0,30.0,40.0,50.0,60.0]:

    M = int(np.round(np.log2(D*k**3.5)))

    N.append(2**M)

# Clock times in mins
clock_times = [34,5*60 + 24,18*60 + 26]

num_cpus = [16,64,512]

k_list = [10.0,20.0,30.0,40.0,50.0,60.0]

# In mins
core_time_per_sample = []

for ii_k in [0,1,2]:
    core_time_per_sample.append(float(clock_times[ii_k]*num_cpus[ii_k])/float(N[ii_k]))

# Claim that core_time_per_sample goes like k^3 (which makes sense)

C = np.mean(np.array(core_time_per_sample)/np.array(k_list[:3])**3)

for ii_k in range(3,6):

    print(ii_k)
    
    k = k_list[ii_k]

    print(k)
    
    time_per_sample = C * k**3

    print(time_per_sample)
    
    total_time = time_per_sample * N[ii_k]

    print(total_time)

    time_on_512 = float(total_time)/512.0

    print(time_on_512)

    print(time_on_512/(60.0*24.0))
