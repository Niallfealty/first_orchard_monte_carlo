# main program
from model.analyser import Analyser

from sys import argv, exit

from config.config              import DEFAULT_NUM_TRIALS, DEFAULT_RAVEN_STEPS_LEFT, DEFAULT_FRUIT_IN_TREE
from functions.input_processing import parse_params

def usage(exit_code):
    print("[#] Welcome to First Orchard Monte Carlo!")
    print("[#] ")
    print("[#] This program can be run without any arguments, in which case it will run")
    print("[#] for the default number of trials ({0}), and the default parameters ".format(DEFAULT_NUM_TRIALS))
    print("[#] for gameplay (DEFAULT_RAVEN_STEPS_LEFT = {0}, DEFAULT_FRUIT_IN_TREE = {1})".format(DEFAULT_RAVEN_STEPS_LEFT, DEFAULT_FRUIT_IN_TREE))
    print("[#] these can be set in the config file (./config/config.py).")
    print("[#] ")
    print("[#] Alternatively you may pass a comma separated list of pairs the number of trials")
    print("[#] and the parameters in brackets, in the format (<trials1>,<params1>),(<trials2>,<params2>)")
    print("[#] (this pattern can be repeated as many times as you like), note that the parameters are ")
    print("[#] fixed as equal at present.abs")
    print("[#] ")
    print("[#] Once complete the program will plot the results and print relevant statistics.")
    exit(exit_code)

def get_args():
    ''' Look for input parameters, looks for a comma
        sep list of (<number of trials>,<parameters>)
    '''
    try:
        num_trials = int(argv[1])
        params = parse_params(argv[2])
    except IndexError:
        try:
            num_trials = int(argv[1])
            params = False
        except IndexError:
            num_trials = DEFAULT_NUM_TRIALS
            params = False
    except ValueError:
        try:
            num_trials = DEFAULT_NUM_TRIALS
            params = parse_params(argv[1])
        except:
            print(e)
            params = False
            if argv[1] in ["-h", "--help"]:
                usage(0)
            else:
                print("[!] Invalid argument: please see help for instructions.")
                usage(1)


    return num_trials, params



if __name__ == '__main__':
    print("[#] Running First Orchard sim") 
    num_trials, params = get_args()
    
    analyser = Analyser()

    if params:
        analyser.run_tests_range(num_trials, params)
        analyser.transform_data_multiple()
        analyser.walk_through_analysis_multi()
        analyser.plot_concat_data()
    else:
        analyser.run_tests(num_trials)
        analyser.plot_outcomes()
        analyser.describe_data()

        
