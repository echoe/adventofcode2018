#!/usr/bin/python/
filepath = 'input.txt'
with open(filepath) as fp:
    lines = fp.readlines()
    for line in lines:
        print line
        mylist = list(line)
