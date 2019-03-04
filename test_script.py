from helmholtz_monte_carlo import error_analysis as err
import pickle


k_range = [30.0,50.0,60.0]

h_spec = (1.0,-1.5)

J_range = [10]

nu = 2

M_range = [10]

delta = 2.0

lambda_mult = 1.0

qoi = 'integral'

# I'm hacking things so that I get the results as they come

for k in k_range:

    print('Quasi Monte Carlo')
    qmc_out = err.investigate_error([k],h_spec,J_range,nu,M_range,'qmc',delta,lambda_mult,qoi,dim=2)

    print('qmc')
    print(qmc_out)
    with open(str(k)+'-qmc.pickle','wb') as f:
        pickle.dump(qmc_out,f)

    print('Monte Carlo')
    mc_out = err.investigate_error([k],h_spec,J_range,nu,M_range,'mc',delta,lambda_mult,qoi,dim=2)

    print('mc')
    print(mc_out)

    with open(str(k)+'-mc.pickle','wb') as f:
        pickle.dump(mc_out,f)





