#!/usr/bin/python/
import sys
import numpy as np
filepath = 'input_test.txt'
overlapping_plots = 0
with open(filepath) as fp:
    lines = fp.readlines()
    #matrix = [['.' for x in range(8)] for y in range(8)]
    matrix = np.zeros( (8,8) )
    used_nums=[]
    print matrix
    print "FIRST"
    for line in lines:
        #plot_overlap = False
        claim_num = line.split(' ')[0].split('#')[1]
        claim_startx = line.split(' ')[2].split(',')[0]
        claim_starty = line.split(' ')[2].split(',')[1].split(':')[0]
        claim_endx = line.split(' ')[3].split('x')[0]
        claim_endy = line.split(' ')[3].split('x')[1]
        print line
        print claim_num, claim_startx, claim_starty, claim_endx, claim_endy
        for x in range(int(claim_startx),int(claim_startx)+int(claim_endx),1):
            for y in range(int(claim_starty),int(claim_starty)+int(claim_endy),1):
                if int(matrix[x,y]) == 0:
                    print "we try to fix ", x, y, 'with current value', matrix[x,y]
                    matrix[x, y]=claim_num
                else:
                    print "we try to X out", x, y, "with false value"
                    matrix[x, y]='20'
        print matrix
print matrix
