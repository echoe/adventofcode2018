#!/usr/bin/python/
import sys
filepath = 'input.txt'
istwonum = 0
isthreenum = 0
with open(filepath) as fp:
    lines = fp.readlines()
    for line in lines:
        istwo=False
        isthree=False
        mylist = list(line)
        for letter in mylist:
            print mylist.count(letter)
            if mylist.count(letter) == 2:
                istwo=True
            if mylist.count(letter) == 3:
                isthree=True
        if istwo == True:
            istwonum = istwonum + 1
        if isthree == True:
            isthreenum = isthreenum + 1
print isthreenum * istwonum
