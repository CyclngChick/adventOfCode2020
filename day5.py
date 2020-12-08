#!/usr/bin/python

import math
import re

infile = open("inputDay5.txt", "r") 
lines = infile.readlines()

# Total number of rows 128 (0 - 127)
# Total columns of seats: 8 (0 - 7)
# F = lower half of numbers
# B = higher half of numbers
# R = higher half of seats
# L = lower half of seats
highestSeatId = 0
lowestSeatId = 913
seatIDlist = []

for line in lines:
    frontRow = 0
    backRow = 127
    lColumn = 0
    rColumn = 7
    print line
    for x in line:
        if x == 'F':
            diff = math.floor((backRow - frontRow) / 2)
            backRow = backRow - diff
        if x == 'B':
            diff = math.ceil((backRow - frontRow) / 2)
            frontRow = frontRow + diff
        if x == 'L':
            diff = round((rColumn - lColumn) / 2)
            rColumn = rColumn - diff
        if x == 'R':
            diff = math.ceil((rColumn - lColumn) / 2)
            lColumn = rColumn - diff
    if re.search("^F", line):
        backRow = backRow - 1
    if re.search("^B", line):
        frontRow = frontRow + 1
    if re.search("[FB]{7}L", line):
        rColumn = rColumn - 1
    if re.search("[FB]{7}R", line):
        lColumn = lColumn + 1
    print("Final seat:")
    print backRow
    print rColumn

    if backRow != frontRow:
        print("THESE ROWS DO NOT MATCH, SOMETHING IS WRONG")
    if rColumn != lColumn:
        print("THESE COLUMNS DO NOT MATCH, SOMETHING IS WRONG")

    seatId = backRow * 8 + rColumn
    print("Seat ID: ", seatId)

    seatIDlist.append(seatId)
    if seatId > highestSeatId:
        highestSeatId = seatId

print("Highest Seat ID: ", highestSeatId)
seatIDlist.sort()
print seatIDlist
