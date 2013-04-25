# Rock paper lizard spock game
# 
# http://en.wikipedia.org/wiki/Rock-paper-scissors-lizard-Spock
#
# Author : Mohammad Rashid
# 24/04/2013 

import argparse
import random

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
parser.description = """
Rock-paper-scissors-lizard-Spock is a five-gesture expansion of the classic selection method game rock-paper-scissors.

**** The rules of Rock-paper-scissors-lizard-Spock are ****

    Scissors cut paper
    Paper covers rock
    Rock crushes lizard
    Lizard poisons Spock
    Spock smashes (or melts) scissors
    Scissors decapitate lizard
    Lizard eats paper
    Paper disproves Spock
    Spock vaporizes rock
    Rock breaks scissors
"""
parser.add_argument('choice', type=str,	help='Valid choices are: rock, spock, paper, lizard, scissors')
args = parser.parse_args()

choices = ("rock", "spock", "paper", "lizard", "scissors")

def is_valid(name):
    if(name in choices):
        return True
    else:
        return False

def rpsls(name):
    name = name.lower()
    cpu_choice = random.randint(0, 4)
    
    if(is_valid(name)):
        player_choice = choices.index(name)
                    
        print ("Player chooses ", name)
        print ("Computer chooses ", choices[cpu_choice])
            
        result = (player_choice - cpu_choice) % 5
        if (result == 0):
            print ("Player and computer tie!")
        elif (result <= 2):
            print ("Player wins!")
        else:
            print ("Computer wins!")
    else:
        print ("Please try again! \nValid choices are : ", " ".join(choices))
    
    print
	
rpsls(args.choice)
