#!/usr/bin/python/
import sys
filepath = 'input.txt'
freq = 0
freqdict = {}
with open(filepath) as fp:
    lines = fp.readlines()    
    for line in lines:
        timestamp = line.split('[')[1].split(']')[0]
        thing = line.split(']')[1].split(' ')[1:]
        freqdict[timestamp]=thing

import pprint
pprint.pprint(freqdict)
