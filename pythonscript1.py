#!/usr/bin/python

print "Hello World!"
myname = 'Me'
myage = 35
myweight = 150
mycity = 'LA'


# This is a while loop with the variable i looping until it is not less than 1000. Identation is CRUCIAL.
i =0
while i < 1000:
	print "This is iteration " ,i
	i=i+1
	print "round and round"
	
	

# With this, since the last line (print "round...) is not idented, it will show up once, it is not part of the while loop.
i =0
while i < 1000:
	print "This is iteration " ,i
	i=i+1
print "round and round"


# loops

family = ['meir', 'leah', 'refael', 'elana', 'daniella', 'aryeh']

for i, person in enumerate(family):
	print "Loop {iteration} is {person}".format(iteration=i, person=person)

