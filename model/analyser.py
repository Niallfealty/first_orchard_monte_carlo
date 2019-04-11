try:
    from model.model import Game
except ImportError:
    from model import Game
    
from pandas import DataFrame, concat

import seaborn                  as sns
from   matplotlib import pyplot as plt

from tqdm         import tqdm

GAME_FIELDS = ["win", "turns"]

class Analyser(object):
    def __init__( self
                , columns = GAME_FIELDS):
        self.data = {} # initialise data
        self.df   = None # for putting a df into
        self.columns = columns
        
        # init for trials across parameters
        self.arg_array     = None
        self.data_multiple = []
        self.df_multiple   = []

    def run_tests(self, number_tests):
        print("[#] Running simulations")
        for trial in tqdm(range(number_tests)):
            self.data[trial] = Game().play_game()

    def run_tests_range(self, number_tests, arg_array):
        ##
        ## arg_array should be an array of tuples: (raven_steps, fruit_in_tree)
        ##
        self.arg_array = arg_array
        print("[#] Running simulations with inputs: {0}".format(arg_array))
        for raven_steps, fruit_in_tree in arg_array:
            data = {}
            for trial in tqdm(range(number_tests)):
                data[trial] = Game( raven_steps_left = raven_steps
                                  , fruit_in_tree    = fruit_in_tree
                                  ).play_game()
                
            self.data_multiple.append(data)

    def transform_data(self):
        self.df         = DataFrame.from_dict(self.data, 'index')
        self.df.columns = self.columns

    def transform_data_multiple(self):
        
        for data_item in self.data_multiple:
            self.df_multiple.append(DataFrame.from_dict(data_item, 'index'))
            
        for df in self.df_multiple:
            df.columns = self.columns

    def plot_outcomes(self):
        if self.df is None: # in case I forget to do this first
            print("[#] Transforming data first")
            self.transform_data()

        outcomes = sns.FacetGrid( self.df
                                , hue = "win")\
                                        .map(sns.distplot,  "turns", kde_kws = {"bw" : 0.5})\
                                                   .add_legend()\
                                                   .despine()\
                                                   .set(alpha=0.6)

        plt.show()

    def plot_outcomes_multi(self, df):
        if df is None: # in case I forget to do this first
            print("[#] Transforming data first")
            self.transform_data_multiple()

        outcomes = sns.FacetGrid( df
                                , hue = "win")\
                                        .map(sns.distplot,  "turns", kde_kws = {"bw" : 0.5})\
                                                   .add_legend()\
                                                   .despine()\
                                                   .set(alpha=0.6)

        plt.show()

    def describe_data(self):
        wins = sum(self.df.win)
        losses = len(self.df.win) - wins

        print("[+] Number of wins:  \t{0}".format(wins))
        print("[+] Number of losses:\t{0}".format(losses))
        print("[+] Max game length: \t{0}".format(self.df.turns.max()))
        print("[+] Min game length: \t{0}".format(self.df.turns.min()))

    def describe_data_multi(self, df):
        wins = sum(df.win)
        losses = len(df.win) - wins

        print("[+] Number of wins:  \t{0}".format(wins))
        print("[+] Number of losses:\t{0}".format(losses))
        print("[+] Max game length: \t{0}".format(df.turns.max()))
        print("[+] Min game length: \t{0}".format(df.turns.min()))


    def walk_through_analysis_multi(self):
        if len(self.df_multiple) == 0:
            self.transform_data_multiple()

        for i in range(len(self.df_multiple)):
            print("[#] Input params: raven_steps = {0}, fruit_in_tree = {1}".format(*self.arg_array[i]))
            self.plot_outcomes_multi(self.df_multiple[i])
            self.describe_data_multi(self.df_multiple[i])

    def merge_multi_df(self):
        for i in range(len(self.df_multiple)):
            self.df_multiple[i]["params"] = str(self.arg_array[i])

        self.df = concat(self.df_multiple)

    def plot_concat_data(self):

        if self.df is None: # in case I forget to do this first
            print("[#] Transforming data first")
            self.merge_multi_df()

        outcomes = sns.FacetGrid( self.df
                                , hue = "win"
                                , row = "params")\
                                        .map(sns.distplot,  "turns", kde_kws = {"bw" : 0.5})\
                                                   .add_legend()\
                                                   .despine()\
                                                   .set(alpha=0.6)
        plt.show()

if __name__ == '__main__':
    print("[#] Testing")
    analyser = Analyser()

    analyser.run_tests_range(5000, [(4,4), (8,8), (10,10)])
    analyser.transform_data_multiple()

    analyser.walk_through_analysis_multi()
    #analyser.plot_outcomes()
    #analyser.describe_data()
