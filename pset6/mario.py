#!/usr/bin/env python

#check the validity of input hight
while True:
    pass
    hight = int(input("Hight:"))
    if hight in range(1, 9):
        break

#print the space and hash that make my shape
for x in range(1, hight+1):
    for y in range(0, hight-x):
        print(" ", end='')
    for z in range(0, x):
        print("#", end='')
    print()

