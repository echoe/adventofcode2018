#!/usr/bin/python/
import sys
filepath = 'input.txt'
overlapping_plots = 0
with open(filepath) as fp:
    lines = fp.readlines()
    matrix = [['.' for x in range(1000)] for y in range(1000)]
    used_nums=[]
    for line in lines:
        #plot_overlap = False
        claim_num = line.split(' ')[0].split('#')[1]
        claim_startx = line.split(' ')[2].split(',')[0]
        claim_starty = line.split(' ')[2].split(',')[1].split(':')[0]
        claim_endx = line.split(' ')[3].split('x')[0]
        claim_endy = line.split(' ')[3].split('x')[1]
        #print line
        #print claim_num, claim_startx, claim_starty, claim_endx, claim_endy
        if claim_num not in used_nums:
            for x in range(int(claim_startx),int(claim_startx)+int(claim_endx),1):
                for y in range(int(claim_starty),int(claim_starty)+int(claim_endy),1):
                    if matrix[x][y]!='.' or matrix[x][y]!='X': # if claim overlaps, count it as one overlap
                        overlapping_plots = overlapping_plots + 1
                        # do not count past 2 claims! those are extraneous
                        matrix[x][y]='X'
                        # plot_overlap = True
                    else: #if claim does not overlap claim it
                        matrix[x][y]=claim_num
        used_nums.append(claim_num)
        #if plot_overlap == True:
        #    overlapping_plots = overlapping_plots + 1
print overlapping_plots
