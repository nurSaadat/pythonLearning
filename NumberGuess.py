"""
The dice game!
a program that rolls a pair of dice and asks the user to guess the sum. If the user's guess is equal to the total value of the dice roll, the user wins! Otherwise, the computer wins.
Write and enjoy.
"""
from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input("Guess a number: "))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "Maximum value is %d" % (max_val)
  guess = get_user_guess()
  if (guess > max_val):
    print ("Your entry should be from 1 to 12")
  else:
    print "Rolling..."
    sleep(2)
    print "First roll: %d" % (first_roll)
    sleep(1)
    print "Second roll: %d" % (second_roll)
    sleep(1)
    total_roll = first_roll + second_roll
    print "%d" % (total_roll)
    print "Result..."
    sleep(1)
    if (total_roll == guess):
      print "Congratulations, You won!"
    else: 
      print "Oops, You lost..."
    
roll_dice(6)
