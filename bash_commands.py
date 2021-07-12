#!/usr/bin/python

# this will run any linux command

import sys
import os 
import subprocess

def RUN(): 
	subprocess.run('''
	for((i=1;i<=$#;i++)); do
	array[i]+=123
    done''',
    shell=True, check=True,
    executable='/bin/bash')

RUN('sleep', '4')
