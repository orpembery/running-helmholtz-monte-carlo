if __name__ == "__main__":
    import pickle
    import numpy as np
    import sys

    # Should really define this elsewhere and import
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
    
    """first entry is h magnitude, second is max M, third is qoi_num - 0 means integral, 1 means point evaluation at origin; fourth is number of shifts, Final entries are different values of k,"""

    k_list = sys.argv[5:]

    h_mag = sys.argv[1]

    max_M = sys.argv[2]

    qoi_num = sys.argv[3]

    num_shifts = sys.argv[4]

    k_C_alpha = [[],[],[]]

    kii = 0
    
    for k in k_list:

        with open('k-'+k+'-h-magnitude-'+h_mag+'-M-'+max_M+'-shifts-'+num_shifts+'-all-qmc-samples.pickle','rb') as f:
            qmc = pickle.load(f)

        # Second entry of QMC is a list
        # Each entry of the list corresponds to a shift
        # And each is itself a list of length 2
        # Each entry of which corresponds to a different QoI
        # And each is itself a list of length (number of samples), containing floats

        num_qois = 2

        all_samples = qmc[1]

        all_approximations = []

        M_low = 2

        M_large_int = int(max_M)

        num_shifts_int = int(num_shifts)

        qoi_num_int = int(qoi_num)

        good_errors = []

        for M in range(M_low,M_large_int+1):

            all_approximations = []

            for iqoi in range(num_qois):

                all_approximations.append([])

                for ishift in range(num_shifts_int):

                    all_approximations[iqoi].append(np.abs(np.array(qmc[1][ishift][iqoi][:(2**M)]).mean()))

            M_out = calculate_qmc_error(all_approximations,num_shifts)

            good_errors.append(M_out[1][qoi_num_int])

            #print(M)
            #print(M_out)

        M_list = list(range(M_low,M_large_int+1))

        #print(M_list)

        #print(good_errors)

        #print(len(M_list))

        #print(len(good_errors))

        #print(list(range(M_large)))

        #p_approx = [ - np.log2(good_errors[ii]/good_errors[ii+1]) for ii in range(M_large_int-M_low)]

        from matplotlib import pyplot as plt

        N_list = 2.0**np.array(M_list)

        N_list_inc_shifts = 20.0 * N_list # Get same convergence rate with this

        loglog = plt.loglog(N_list,good_errors,'.')

        # Add line of best fit
        # Am I using the right log?

        fit = np.polyfit(np.log10(N_list),np.log10(good_errors),deg=1)

        #print(np.log(N_list))

        #    print(np.log(good_errors))

        #print('Slope of line of best fit:')
        #print(fit[0])

        k_C_alpha[0].append(float(k))
        k_C_alpha[1].append(10.0**fit[1])
        k_C_alpha[2].append(fit[0])
        
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

        num_sig_fig = 6
        
        plt.loglog(x_for_fit,y_for_fit,'--',color=loglog[-1].get_color(),label='k='+k+': C = '+str(k_C_alpha[1][kii])[:num_sig_fig] + ', alpha = '+str(k_C_alpha[2][kii])[:num_sig_fig])

        kii += 1

    plt.xlabel('N')

    plt.ylabel('QMC Error')

    k_title = str(k_list)

    if qoi_num == '1':
        qoi_string = 'point_evaluation at origin'
    elif qoi_num == '0':
        qoi_string = 'integral of solution'


    plt.title('QMC error for '+ qoi_string +' for k = '+k_title)


        #    plt.plot([np.log(N_list[0]),np.log(N_list[-1])],[np.log(good_errors[0]),np.log(good_errors[0])-(np.log(N_list[-1])-np.log(N_list[0]))]) # What is this?







        #print(len(p_approx))

        #print(p_approx)

        # For each QoI:

        # For each shift, just take the mean

        # Then calculate the overall mean

        # Then calculate the error for each QoI
    plt.legend()
    plt.show()
    print(k_C_alpha)

    plt.loglog(k_C_alpha[0],k_C_alpha[1],'rx')
    plt.title('C against k, for qoi = '+qoi_string)
    plt.xlabel('k')
    plt.ylabel('C')
    plt.show()

    plt.plot(k_C_alpha[0],-np.array(k_C_alpha[2]),'rx')
    plt.title('alpha against k for qoi = '+qoi_string)
    plt.xlabel('k')
    plt.ylabel('alpha')
    plt.show()
