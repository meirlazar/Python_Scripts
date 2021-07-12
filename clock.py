#!/usr/bin/python
# Author: Meir Lazar
# Date: 7/11/2016
# Purpose: Basic clock script


print "----Clock Script----"

while len(CS) -ne 2: do  CS = input("What second is it? "): done  # len() will tell the char length
while len(CM) -ne 2: do  CM = input("What minute is it? "): done
while len(CH) -ne 2: do  CH = input("What hour is it? "): done

print "The first number of the seconds is", CS[0]
print "The first two number of the minute is", CM[0:2]

for letter in CH: print letter: done

if CH >= 24: print CH, "is wrong, it must be less than 24"

print "The current time is",CH,":",CM,":",CS, "seconds"




#END

