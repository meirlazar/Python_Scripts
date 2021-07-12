#!/usr/bin/python

import random

# This script plays a game of rolling as many dice as you specify until it hits all the same numbers 

print('Hello Player')
DICE = input("Please enter number of dice: ")
print "OK, I will use", DICE, "dice"

def rollthedice(items):
	Y = [random.randint(1,6) for _ in range(items)]
	return Y

def all_same(items):
	Z = all(x == items[0] for x in items)
	return Z
	
i=0
YAHTZEE = 'nope'

while YAHTZEE != True:
	i = i + 1
	diceroll = rollthedice(DICE)
	print "On Roll Number", i, "you rolled", diceroll
	YAHTZEE = all_same(diceroll)
	print (YAHTZEE)
	
print('Yahtzee!!!')
	
