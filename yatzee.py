#!/usr/bin/python

import random


# This script plays a game of rolling as many dice as you specify until it hits all the same numbers 

print('Hello Player')
DICE = input("Please enter number of dice: ")
print "OK, I will use", DICE, "dice"

def all_same(items):
	Y = all(x == items[0] for x in items)
	return Y
	
i=0
YAHTZEE = 'nope'

while YAHTZEE != True:
	i = i + 1
	theroll=[random.randint(1,6) for _ in range(DICE)]
	print "On Roll Number", i, "you rolled", theroll
	YAHTZEE = all_same(theroll)
	print (YAHTZEE)
	
print('Yahtzee!!!')
	
