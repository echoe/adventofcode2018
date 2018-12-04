#!/usr/bin/python/
import sys
import datetime as dt
filepath = 'input.txt'
freq = 0
freqdict = {}
with open(filepath) as fp:
    lines = fp.readlines()    
    for line in lines:
        timestamp = line.split('[')[1].split(']')[0]
        thing = line.split(']')[1].split(' ')[1:]
        freqdict[timestamp]=thing

guardnum=0
falls=0
wakes=0
guardtimedict = {}
guardmindict = {}
for keys in sorted(freqdict):
    values = freqdict[keys]
    print(keys)
    if values[0]=="Guard":
        guardnum = values[1].split('#')[1]
    elif values[0]=="falls":
        falls = keys.split(' ')[1].split(':')[1]
    elif values[0]=="wakes":
        wakes = keys.split(' ')[1].split(':')[1]
        totalsleep = int(wakes) - int(falls)
        try:
            guardtimedict[guardnum] = int(guardtimedict[guardnum]) + int(totalsleep)
        except KeyError:
            guardtimedict[guardnum] = int(totalsleep)
        for i in range(int(falls), int(wakes)):
            try:
                guardmindict[guardnum, i] = guardmindict[guardnum, i] + 1
            except KeyError:
                guardmindict[guardnum, i] = 1

print guardtimedict
highval = 0
highguard = 0
for keys, values in guardtimedict.items():
    if int(values) > highval:
        highguard = keys
        highval = int(values)
print guardmindict
highmin = 0
newhighval = 0
for keys, values in guardmindict.items():
    if keys[0] == highguard:
        if int(values) > newhighval:
            highmin = keys[1]
            newhighval = int(values)

print "guard", highguard, 'sleeps for', highval, "minutes. on minute", highmin, "they were asleep", newhighval, "times"
print "so the answer to part 1 is", int(highguard)*int(highmin)

newhighmin = 0
newhighguard = 0
newnewhighval = 0
for keys, values in guardmindict.items():
    if int(values) > newnewhighval:
        newhighguard = keys[0]
        newhighmin = keys[1]
        newnewhighval = int(values)
print "really though guard", newhighguard, "sleeps on minute", newhighmin, "the most, it's ", newnewhighval, "times"
print "so part 2 is", int(newhighguard)*int(newhighmin)
