from config.config import DEFAULT_RAVEN_STEPS_LEFT, DEFAULT_FRUIT_IN_TREE

from random import randint
import numpy as np

class Dice(object):
    def __init__( self
                , outcomes = ["Red", "Green", "Yellow", "Blue","Basket","Raven"]
                ):
        self.outcomes = outcomes

    def roll(self):
        return self.outcomes[randint(0,5)]


class Game(object):
    def __init__(self
                , raven_steps_left = DEFAULT_RAVEN_STEPS_LEFT
                , fruit_in_tree    = DEFAULT_FRUIT_IN_TREE
                ):

        # initialise game variables
        self.raven        = raven_steps_left
        self.red_fruit    = fruit_in_tree
        self.green_fruit  = fruit_in_tree
        self.blue_fruit   = fruit_in_tree
        self.yellow_fruit = fruit_in_tree
        
        # def dice
        self.dice         = Dice()
        
        # state tracking
        self.turns = 0
        
        self.game_in_play = True
        self.win          = False

    def play_game(self):
        #print("[+] Starting game!")
        while(self.game_in_play):
            self.take_turn()
        
        return (self.win, self.turns)
    
        #print("[+] Game completed in {0} turns".format(self.turns))

        #if self.win:
        #    print("[+] Outcome: WIN!!!")
        #else:
        #    print("[-] Outcome: LOSS. :-(")

    def take_turn(self):
        if (self.raven > 0):
            if self.sum_fruit() > 0:
                self.turns += 1
                
                dice_roll = self.dice.roll()

                if not self._roll_dice_accounting(dice_roll):
                    raise ValueError("[!] Dice roll returned value incompatible with game.")
                #else:
                #    print(dice_roll)
            else:
                self.game_in_play = False
                self.win          = True
        else:
            self.game_in_play = False

    def _roll_dice_accounting(self, dice_roll):
        if dice_roll == "Red":
            self._roll_red()
        elif dice_roll == "Green":
            self._roll_green()
        elif dice_roll == "Blue":
            self._roll_blue()
        elif dice_roll == "Yellow":
            self._roll_yellow()
        elif dice_roll == "Basket":
            self._remove_most_remaining()
        elif dice_roll == "Raven":
            self._step_raven()
        else:
            return False # something went wrong

        return True


    def _roll_red(self):
        if self.red_fruit > 0:
            self.red_fruit -= 1

    def _roll_green(self):
        if self.green_fruit > 0:
            self.green_fruit -= 1

    def _roll_blue(self):
        if self.blue_fruit > 0:
            self.blue_fruit -= 1

    def _roll_yellow(self):
        if self.yellow_fruit > 0:
            self.yellow_fruit -= 1

    def _remove_most_remaining(self):
        # this function looks odd but finds the highest count and uses that to call the decrement func
        counts    = [self.red_fruit, self.green_fruit, self.blue_fruit, self.yellow_fruit]
        functions = [self._roll_red, self._roll_green, self._roll_blue, self._roll_yellow]

        functions[np.argmax(counts)]()

    def _step_raven(self):
        if self.raven > 0:
            self.raven -= 1

    def sum_fruit(self):
        return sum([self.red_fruit, self.green_fruit, self.blue_fruit, self.yellow_fruit])


if __name__ == "__main__":
    print("[#] Running tests")
    game = Game()
    #for test in range(20):
    #    game.take_turn()
    game.play_game()
