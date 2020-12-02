#!/usr/bin/python

import math

infile = open("inputDay2.txt", "r") 

#lines = [line.rstrip('\n') for line in infile]

lines = infile.readlines()

validPassword = 0
invalidPassword = 0


## Part 1
#for line in lines:
#    print line
#    input = line.split()
#    value = input[0]
#    splitValue = value.split('-')
#    lowValue = int(splitValue[0])
#    print("lowValue: ", lowValue)
#    highValue = int(splitValue[1])
#    print("highValue: ", highValue)
#    letterColon = input[1].split(':')
#    letter = letterColon[0]
#    print("Letter: ", letter)
#    password = input[2]
#    print("Password: ", password)
#    instanceNum = 0
#    for x in password:
#        if letter == x:
#            instanceNum = instanceNum + 1
#    if lowValue <= instanceNum <= highValue:
#        validPassword = validPassword + 1
#        print("This password is valid!")
#    else:
#        invalidPassword = invalidPassword + 1
#
#print("Number of valid passwords: ", validPassword)


## Part 2
for line in lines:
    print line
    input = line.split()
    value = input[0]
    splitValue = value.split('-')
    firstValue = int(splitValue[0])
    print("firstValue: ", firstValue)
    secondValue = int(splitValue[1])
    print("secondValue: ", secondValue)
    letterColon = input[1].split(':')
    letter = letterColon[0]
    print("Letter: ", letter)
    password = input[2]
    print("Password: ", password)

    firstInstance = False
    secondInstance = False

    if password[firstValue - 1] == letter:
        print("First instance is correct!")
        firstInstance = True
    if password[secondValue - 1] == letter:
        print("Second instance is correct!")
        secondInstance = True

    if firstInstance != secondInstance:
        validPassword = validPassword + 1
        print("This password is valid!")
    else:
        invalidPassword = invalidPassword + 1

print("Number of valid passwords: ", validPassword)