if __name__ == "__main__":
    import pickle
    import numpy as np

    def calculate_qmc_error(all_approximations,nu):
        """ Calculates the QMC error for the inputted list."""

        # all_approximations should be a list of length num_qois

        # Each entry all_approximations[ii] should be a list of length num_shifts

        # Each entry of all_approximations[ii] should be the average, for that shift, of that QoI

        all_approximations = [np.array(approximation) for approximation in all_approximations]
                
        # Calculate the QMC approximations for each qoi
        approx = [approximation.mean() for approximation in all_approximations]
    
        # Calculate the error for each qoi - formula taken from
        # [Graham, Kuo, Nuyens, Scheichl, Sloan, JCP
        # 230, pp. 3668-3694 (2011), equation (4.6)]
        error = [np.sqrt(((approx[ii]-all_approximations[ii])**2).sum()\
                         /(float(nu)*(float(nu)-1.0))) for ii in range(num_qois)]

        
        return [approx,error]

    M_large = 6

    qoi_num = 1 # 0 = point evaluation at the origin, 1 means integral (in current setup), changed from previosu versions
    

    with open('k-5.0-h-magnitude-0.25-M-'+str(M_large)+'-all-qmc-samples.pickle','rb') as f:
        qmc = pickle.load(f)

    # Second entry of QMC is a list
    # Each entry of the list corresponds to a shift
    # And each is itself a list of length 2
    # Each entry of which corresponds to a different QoI
    # And each is itself a list of length 1024, containing floats

    num_qois = 2

    num_shifts = 20

    all_samples = qmc[1]

    all_approximations = []

    M_low = 2

    good_errors = []

    for M in range(M_low,M_large+1):

        all_approximations = []
        
        for iqoi in range(num_qois):

            all_approximations.append([])

            for ishift in range(num_shifts):
                
                all_approximations[iqoi].append(np.abs(np.array(qmc[1][ishift][iqoi][:(2**M)]).mean()))

        M_out = calculate_qmc_error(all_approximations,num_shifts)

        good_errors.append(M_out[qoi_num][1])
        
        print(M)
        print(M_out)
            
    M_list = list(range(M_low,M_large+1))

    print(M_list)

    print(good_errors)
    
    print(len(M_list))

    print(len(good_errors))

    print(list(range(M_large)))
    
    p_approx = [ - np.log2(good_errors[ii]/good_errors[ii+1]) for ii in range(M_large-M_low)]

    from matplotlib import pyplot as plt

    N_list = 2.0**np.array(M_list)

    N_list_inc_shifts = 20.0 * N_list # Get same convergence rate with this
    
    plt.loglog(N_list,good_errors)

    plt.xlabel('log(N)')

    plt.ylabel('log(QMC Error)')

    plt.title('QMC error for point evaluation at origin for k = 5')

#    plt.plot([np.log(N_list[0]),np.log(N_list[-1])],[np.log(good_errors[0]),np.log(good_errors[0])-(np.log(N_list[-1])-np.log(N_list[0]))])
    
    plt.show()

    

    print(len(p_approx))
    
    print(p_approx)
        
    # For each QoI:

    # For each shift, just take the mean

    # Then calculate the overall mean

    # Then calculate the error for each QoI
