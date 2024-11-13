#ex7
# Simulate rolling two dice, three times.  Prints
# the results of each die roll.  This program is used
# to show how variable scope works.

#solution:
import random    #import library

def roll_dice():
  die1=random.randint(1,6)
  die2=random.randint(1,6)
  return die1,die2


roll_dice()

    
  