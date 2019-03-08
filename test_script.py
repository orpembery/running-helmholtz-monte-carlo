from helmholtz_monte_carlo import error_analysis as err
import pickle


k_range = [10.0,20.0,30.0]

h_spec = (1.0,-1.5)

J = 10

nu = 20

M = 10

delta = 1.0

lambda_mult = 1.0

qois = ['integral','origin']

# I'm hacking things so that I get the results as they come

for k in k_range:

    print('Quasi Monte Carlo')
    qmc_out = err.investigate_error(k,h_spec,J,nu,M,'qmc',delta,lambda_mult,qois,dim=2,display_progress=True)

    print('qmc')
    print(qmc_out)
    with open(str(k)+'-qmc.pickle','wb') as f:
        pickle.dump(qmc_out,f)

    print('Monte Carlo')
    mc_out = err.investigate_error(k,h_spec,J,nu,M,'mc',delta,lambda_mult,qois,dim=2,display_progress=True)

    print('mc')
    print(mc_out)

    with open(str(k)+'-mc.pickle','wb') as f:
        pickle.dump(mc_out,f)





