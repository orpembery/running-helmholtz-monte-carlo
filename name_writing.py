def name_writing(quants):
    """Creates the parameter-specific part of the folder name we use.

    Input - dict - a dict containing all the parameter values we want to use in the filename.

    If a key in the dict is "qois", then this is not included in the folder name.

    Output - string - the string to go into the folder name.
    """

    folder_name = ''

    for key in sorted(quants.keys()):
        if key is not 'qois':
            folder_name += '-' + key + '-' + str(quants[key])
        else:
            folder_name += '-' + key
            for string in quants[key]:
                folder_name += '-' + string

    folder_name = folder_name[1:] # Has erroneous dash at the start

    return folder_name

def make_quants(sys_args):
    """Takes in sys.argv[1:] (in investigate_convergence), and returns a dict with everything done
    correctly for investigate_convergence."""

    quantity_names = ['k','h_levels','M_high','nu','J','delta','lambda_mult','j_scaling','dim','on_balena','qois']

    num_non_qoi_quants = len(quantity_names)-1

    quants = { quantity_names[ii]:sys_args[ii] for ii in range(num_non_qoi_quants)}

    quants[quantity_names[-1]] = sys_args[(num_non_qoi_quants):] 

    # Need to convert things from strings to the right types
    
    quants['k'] = float(quants['k'])

    quants['h_levels'] = int(quants['h_levels'])

    quants['M_high'] = int(quants['M_high'])

    quants['nu'] = int(quants['nu'])

    quants['J'] = int(quants['J'])

    quants['delta'] = float(quants['delta'])

    quants['lambda_mult'] = float(quants['lambda_mult'])

    quants['j_scaling'] = float(quants['j_scaling'])

    quants['dim'] = int(quants['dim'])

    if quants['on_balena'] is not '*': # This is a wildrcard used in analysis
        quants['on_balena'] = bool(int(quants['on_balena']))

    return quants
