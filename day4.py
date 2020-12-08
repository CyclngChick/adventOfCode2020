#!/usr/bin/python

import math
import re

infile = open("inputDay4.txt", "r") 
lines = infile.readlines()

currentPassport = ''
validPassports = 0

# Necessary fields:
#byr (Birth Year) - four digits; at least 1920 and at most 2002.
#iyr (Issue Year) - four digits; at least 2010 and at most 2020.
#eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
#hgt (Height) - a number followed by either cm or in:
#If cm, the number must be at least 150 and at most 193.
#If in, the number must be at least 59 and at most 76.
#hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
#ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
#pid (Passport ID) - a nine-digit number, including leading zeroes.

#cid (Country ID) - ignored, missing or not.


for line in lines:
    if line != '\n':
        currentPassport = currentPassport + ' ' + line.rstrip('\n')
    else:
        currentPassport = ''
    byr = re.findall("(byr:)([1-2][0-9]{3})", currentPassport)
    if byr:
        if 1920 <= int(byr[0][1]) <= 2002:
            #print("Birth year valid.")
            iyr = re.findall("(iyr:)(20[0-9]{2})", currentPassport)
            if iyr:
                if 2010 <= int(iyr[0][1]) <= 2020:
                    #print("Issue year valid.")
                    eyr = re.findall("(eyr:)(20[0-9]{2})", currentPassport)
                    if eyr:
                        if 2020 <= int(eyr[0][1]) <= 2030:
                            #print("Expiration year valid.")
                            hgtIn = re.findall("(hgt:)([0-9]{2,3})(cm|in)", currentPassport)
                            if hgtIn:
                                if (str(hgtIn[0][2]) == 'cm' and 150 <= int(hgtIn[0][1]) <= 193) or (str(hgtIn[0][2]) == 'in' and 59 <= int(hgtIn[0][1]) <= 76):
                                    #print("Height valid.")
                                    if re.search("hcl:#[0-9a-f]{6}", currentPassport) != None:
                                        #print("Hair color valid.")
                                        if re.search("ecl:(amb|blu|brn|gry|grn|hzl|oth){1}", currentPassport) != None:
                                            #print("Eye color valid.")
                                            if re.search("pid:[0-9]{9}", currentPassport)!= None:
                                                validPassports = validPassports + 1
                                                print hgtIn
                                                print currentPassport
                                                currentPassport = ''

print("Number of valid passports: ", validPassports)