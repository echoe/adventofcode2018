#!/usr/bin/python/
import sys
filepath = 'input.txt'
linearray = []
#create array of all lines in input
with open(filepath) as fp:
    lines = fp.readlines()
    for line in lines:
        #print line
        linearray.append(line)

#print linearray

for line in linearray:
    for line2 in linearray:
        if line != line2:
            for i in range(25):
                if ''.join(line[0:i]+line[i+1:25]) == ''.join(line2[0:i]+line2[i+1:25]):
                    print ''.join(line[0:i]+line[i+1:25]), ''.join(line2[0:i]+line2[i+1:25])
                    print ''.join(line), ''.join(line2)
                    sys.exit()
