if __name__ == "__main__":
    import pickle
    import numpy as np
    import sys

    """First entry is k, second is h magnitude, third is max M, fourth is qoi_num - 0 means integral, 1 means point evaluation at origin."""

    k = sys.argv[1]
    
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


    with open('k-'+k+'-h-magnitude-'+sys.argv[2]+'-M-'+sys.argv[3]+'-all-qmc-samples.pickle','rb') as f:
        qmc = pickle.load(f)

    # Second entry of QMC is a list
    # Each entry of the list corresponds to a shift
    # And each is itself a list of length 2
    # Each entry of which corresponds to a different QoI
    # And each is itself a list of length (number of samples), containing floats

    num_qois = 2

    num_shifts = 20

    all_samples = qmc[1]

    all_approximations = []

    M_low = 2

    M_large = 11

    good_errors = []

    qoi_num =  int(sys.argv[4])# 1 = point evaluation at the origin, 0 means integral (in current setup)

    for M in range(M_low,M_large+1):

        all_approximations = []
        
        for iqoi in range(num_qois):

            all_approximations.append([])

            for ishift in range(num_shifts):

                all_approximations[iqoi].append(np.abs(np.array(qmc[1][ishift][iqoi][:(2**M)]).mean()))

        M_out = calculate_qmc_error(all_approximations,num_shifts)

        good_errors.append(M_out[1][qoi_num])
        
        #print(M)
        #print(M_out)
            
    M_list = list(range(M_low,M_large+1))

    #print(M_list)

    #print(good_errors)
    
    #print(len(M_list))

    #print(len(good_errors))

    #print(list(range(M_large)))
    
    p_approx = [ - np.log2(good_errors[ii]/good_errors[ii+1]) for ii in range(M_large-M_low)]

    from matplotlib import pyplot as plt

    N_list = 2.0**np.array(M_list)

    N_list_inc_shifts = 20.0 * N_list # Get same convergence rate with this
    
    plt.loglog(N_list,good_errors,'x')

    # Add line of best fit
    # Am I using the right log?
    
    fit = np.polyfit(np.log10(N_list),np.log10(good_errors),deg=1)

    #print(np.log(N_list))

    #    print(np.log(good_errors))

    print('Slope of line of best fit:')
    print(fit[0])
    
    #print(fit)
    
    # entry 0 is intercept, 1 is gradient

    # There must be an easy way to do this
    
    big_N = max(N_list)

    small_N = min(N_list)
    
    x_for_fit = [small_N,big_N]

    y_for_fit = [10.0**(fit[1]+fit[0]*np.log10(small_N)),10.0**(fit[1]+fit[0]*np.log10(big_N))]

    #print(N_list)

    #print(good_errors)
    
    #print(x_for_fit)

    #print(y_for_fit)
    
    plt.loglog(x_for_fit,y_for_fit,'--')
    
    plt.xlabel('log(N)')

    plt.ylabel('log(QMC Error)')

    if qoi_num == 1:
        plt.title('QMC error for point evaluation at origin for k = '+k)
    elif qoi_num == 0:
        plt.title('QMC error for integral of solution for k = '+k)

    #    plt.plot([np.log(N_list[0]),np.log(N_list[-1])],[np.log(good_errors[0]),np.log(good_errors[0])-(np.log(N_list[-1])-np.log(N_list[0]))]) # What is this?



    plt.show()

    

    #print(len(p_approx))
    
    #print(p_approx)
        
    # For each QoI:

    # For each shift, just take the mean

    # Then calculate the overall mean

    # Then calculate the error for each QoI
