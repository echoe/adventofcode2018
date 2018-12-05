#!/usr/bin/python/
import sys
filepath = 'input.txt'
with open(filepath) as fp:
    data = list(fp.readline())
    del data[-1]

total_reactions = 0
while True:
    reactions = False
    prev_letter = ''
    my_list_part = 0
    print total_reactions
    for letter in data:
        if prev_letter == letter.swapcase():
            #print "we have", data, "at list part", my_list_part
            del data[my_list_part-1]
            del data[my_list_part-1]
            total_reactions = total_reactions+1
            reactions = True
            #print "we removed the reacting parts of the list and now have", data, ". back to the start"
            break
        prev_letter = letter
        my_list_part=my_list_part+1
    if reactions == False:
        break

print data
print len(data)
