#!/usr/bin/python/
import sys
filepath = 'input.txt'
freq = 0
freqarray = []
result = []
with open(filepath) as fp:
    lines = fp.readlines()    
    while True:
        for line in lines:
            freq = freq + int(line)
            if freq in freqarray:
                print freq
                sys.exit()
            else:
                freqarray.append(freq)
