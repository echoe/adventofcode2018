#!/usr/bin/python/
import sys
import string
filepath = 'input.txt'
with open(filepath) as fp:
    initialdata = list(fp.readline())
    del initialdata[-1]

total_reactions = 0
best_result = ''
best_result_num = 50000
for alpha in list(string.ascii_lowercase):
    data = initialdata[:]
    data[:] = (value for value in data if value != alpha)
    data[:] = (value for value in data if value != alpha.upper())
    #print data
    while True:
        reactions = False
        prev_letter = ''
        my_list_part = 0
        #print total_reactions
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
            if len(data) < best_result_num:
                best_result_num = len(data)
                best_result = alpha
            break
    #print 'removing ', alpha, 'produces a length of', len(data)

print 'removing ', best_result, 'is the best result. it prodces a length of ', best_result_num
