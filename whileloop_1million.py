#!/usr/bin/python

import time
startTime = time.time()

i=0
while (i < 1000000):
	i = i + 1
	print (i)

print i
executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))

