#!/usr/bin/python

import math
import re

infile = open("inputDay6.txt", "r") 
lines = infile.read()
answers = lines.split('\n\n')
totalAnswers = 0

print answers
output = []

# Part 1
#for answer in answers:
#    print answer
#    new_string = " ".join(answer.splitlines())
#    print new_string
#    best = new_string.replace(" ", "")
#    output.append(best)
#
#print output
#
#for x in output:
#    #print x
#    #print("Original length: ", len(x))
#    a = list(set(x))
#    #print a
#    #print("Deduplicated length: ", len(a))
#    totalAnswers = totalAnswers + len(a)
#
#print("Total answers: ", totalAnswers)

# Part 2
for answer in answers:
    print answer
    a = answer.splitlines()
    print a
    res = set.intersection(*map(set, a))
    totalAnswers = totalAnswers + len(res)


print("Total answers: ", totalAnswers)