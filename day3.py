#!/usr/bin/python

import math

infile = open("inputDay3.txt", "r") 
lines = infile.readlines()

# Part 1
# Movement: right 3, down 1
#treesHit = 0
#currentSpot = 0
#
#for line in lines:
#    currentLine = line.rstrip()
#    for x in range(32):
#        currentLine = currentLine + line.rstrip()
#    if currentLine[currentSpot] == '#':
#        treesHit = treesHit +1
#    currentSpot = currentSpot + 3
#
#print("Number of trees Hit: ", treesHit)



# Part 2
# Movement: right 1, down 1
treesHit1 = 0
currentSpot = 0
currentLine = ''

for line in lines:
    currentLine = line.rstrip()
    for x in range(32):
        currentLine = currentLine + line.rstrip()
    if currentLine[currentSpot] == '#':
        treesHit1 = treesHit1 +1
    currentSpot = currentSpot + 1

print("Number of trees Hit(+1): ", treesHit1)
# 90

# Movement: right 3, down 1
treesHit3 = 0
currentSpot = 0
currentLine = ''

for line in lines:
    currentLine = line.rstrip()
    for x in range(32):
        currentLine = currentLine + line.rstrip()
    if currentLine[currentSpot] == '#':
        treesHit3 = treesHit3 +1
    currentSpot = currentSpot + 3

print("Number of trees Hit (+3): ", treesHit3)
# 244

# Movement: right 5, down 1
treesHit5 = 0
currentSpot = 0
currentLine = ''

for line in lines:
    currentLine = line.rstrip()
    for x in range(150):
        currentLine = currentLine + line.rstrip()
    if currentLine[currentSpot] == '#':
        treesHit5 = treesHit5 +1
    currentSpot = currentSpot + 5

print("Number of trees Hit (+5): ", treesHit5)
# 97

# Movement: right 7, down 1
treesHit7 = 0
currentSpot = 0
currentLine = ''

for line in lines:
    currentLine = line.rstrip()
    for x in range(300):
        currentLine = currentLine + line.rstrip()
    if currentLine[currentSpot] == '#':
        treesHit7 = treesHit7 +1
    currentSpot = currentSpot + 7

print("Number of trees Hit (+7): ", treesHit7)
# 92
# Movement: right 1, down 2
everyOther = 2
treesHit2 = 0
currentSpot = 0
currentLine = ''

for line in lines:
    if everyOther % 2 == 0:
        currentLine = line.rstrip()
        for x in range(30):
            currentLine = currentLine + line.rstrip()
        if currentLine[currentSpot] == '#':
            treesHit2 = treesHit2 +1
        currentSpot = currentSpot + 1
    else:
        nothing = 0
    everyOther = everyOther + 1

print("Number of trees Hit (+2 down): ", treesHit2)
# 48

total = treesHit1 * treesHit3 * treesHit5 * treesHit7 * treesHit2

print("Total trees hit: ", total)