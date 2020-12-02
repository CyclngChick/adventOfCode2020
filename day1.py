#!/usr/bin/python

import math

infile = open("inputDay1.txt", "r") 

lines = [line.rstrip('\n') for line in infile]

## Part 1
#for line in lines:
#    #print('line= ', line)
#    for value in lines:
#        #print('value= ', value)
#        if (int(line) + int(value)) == 2020:
#            print('Found it!')
#            print line
#            print value
#            input1 = int(line)
#            input2 = int(value)
#
#expenseTotal = input1 * input2
#
#print('Your expense account total was: ')
#print expenseTotal


## Part 2
for line in lines:
    #print('line= ', line)
    for value in lines:
        #print('value= ', value)
        for third in lines:
            if (int(line) + int(value) + int(third)) == 2020:
                print('Found it!')
                print line
                print value
                print third
                input1 = int(line)
                input2 = int(value)
                input3 = int(third)

expenseTotal = input1 * input2 * input3

print('Your expense account total was: ')
print expenseTotal