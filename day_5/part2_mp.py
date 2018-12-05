#!/usr/bin/python/
import sys
import string
from multiprocessing import Pool
filepath = 'input.txt'
with open(filepath) as fp:
    initialdata = list(fp.readline())
    del initialdata[-1]

bestone=50000
def checkfunction(alpha):
    data = initialdata[:]
    data[:] = (value for value in data if value != alpha)
    data[:] = (value for value in data if value != alpha.upper())
    #print data
    while True:
        reactions = False
        prev_letter = ''
        my_list_part = 0
        for letter in data:
            if prev_letter == letter.swapcase():
                #print "we have", data, "at list part", my_list_part
                del data[my_list_part-1]
                del data[my_list_part-1]
                reactions = True
                #print "we removed the reacting parts of the list and now have", data, ". back to the start"
                break
            prev_letter = letter
            my_list_part=my_list_part+1
        if reactions == False:
            break
    print 'removing ', alpha, 'produces a length of', len(data)
    return len(data)

p = Pool()
bestone = 50000
for i in p.map(checkfunction, list(string.ascii_lowercase)):
    if i < bestone:
        bestone = i
print bestone
