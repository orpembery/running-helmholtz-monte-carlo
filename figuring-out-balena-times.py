import numpy as np

# Figuring out number of QMC points:

exponent_old = 3.5

exponent_new = 0.28

num_cores = 64

D_old = 2048/(10.0**exponent_old)

D_new = 2048/(10.0**exponent_new)

N_old = []

N_new = []

for k in [10.0,20.0,30.0,40.0,50.0,60.0]:

    M = int(np.round(np.log2(D_old*k**exponent_old)))

    N_old.append(2**M)

    M = int(np.round(np.log2(D_new*k**exponent_new)))

    N_new.append(2**M)

# Clock times in mins
clock_times = [34,5*60 + 24,18*60 + 26]

num_cpus = [16,64,512]

k_list = [10.0,20.0,30.0,40.0,50.0,60.0]

# In mins
core_time_per_sample = []

for ii_k in [0,1,2]:
    core_time_per_sample.append(float(clock_times[ii_k]*num_cpus[ii_k])/float(N_old[ii_k]))

# Claim that core_time_per_sample goes like k^3 (which makes sense)

C = np.mean(np.array(core_time_per_sample)/np.array(k_list[:3])**3)

for ii_k in range(6):

    print(ii_k)
    
    k = k_list[ii_k]

    print('k',k)

    print('Number of samples',N_new[ii_k])
    
    time_per_sample = C * k**3

    #print(time_per_sample)
    
    total_time = time_per_sample * N_new[ii_k]

    print('total time in minutes',total_time)

    time_on_16 = float(total_time)/float(num_cores)

    print('total_time on '+str(num_cores)+' cores in minutes',time_on_16)

    print('total_time on '+str(num_cores)+' cores in days',time_on_16/(60.0*24.0))
