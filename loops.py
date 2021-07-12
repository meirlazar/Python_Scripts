#!/usr/bin/python

# loops

family = ['meir', 'leah', 'refael', 'elana', 'daniella', 'aryeh']

for i, person in enumerate(family):
	print "Loop {iteration} is {person}".format(iteration=i, person=person)
