#!/usr/bin/python

# This script plays a game of rolling as many dice as you specify until it hits all the same numbers 

import subprocess
import random 
#import time

def clear(): 
	subprocess.call("clear")
	
def sleep(items): 
	subprocess.call(['sleep', '{0}'.format(items)])

DICE = input("Hello Player. Please enter number of dice: ")
clear()
print "OK, I will roll", DICE, "dice until they all roll identical numbers"
sleep(5)

i=0
YAHTZEE = 'nope'

while YAHTZEE != True:
	i = i + 1
	theroll=[random.randint(1,6) for _ in range(DICE)]
	print "Roll:", i, "I rolled", theroll
	YAHTZEE = (len(set(theroll)) == 1)
	
print 'Yahtzee!!! The dice rolled all:',theroll[1]
