#!/usr/bin/python3
# Purpose: Basic clock script

import time
import os

sec = int(input("What second is it?: "))
min = int(input("What minute is it?: "))
hr = int(input("What hour is it?: "))
ampm = str(input("AM or PM: "))

while True: 
	
	if sec == 60:
		sec = 0
		min = min + 1
	
	if min == 60:
		min = 0
		hr = hr + 1
	
	if hr == 12 and min == 0 and sec == 0:
		if ampm == "AM":
			ampm = "PM"
		elif ampm == "PM":
			ampm = "AM"
	
	if hr == 13:
		hr = 1
	
	os.system('clear')
	print(f"Current Time: {hr:02d}:{min:02d}:{sec:02d} {ampm}")
	time.sleep(1)
	os.system('clear')
	sec = sec + 1
