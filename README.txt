# first_orchard_monte_carlo

A Monte Carlo simulation of the children's game First Orchard (https://www.habausa.com/my-very-first-games-first-orchard/).

Config file includes parameters for the default number of trials and the default number of steps for the raven and fruit in the tree

the first arg (and only) you can pass is and comma separated list of parameters for trials, you can pass as many as you like and the pairs should be the number of trials in the first position and the raven steps/fruits per tree in the second, as follows:

python3 main.py (<trials1>,<params1>),(<trials2>,<params2>),(<trials3>,<params3>)

with <trials>,<params> = integers
