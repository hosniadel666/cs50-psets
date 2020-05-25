#!/usr/bin/env python
from cs50 import get_float
import sys
a = 25
b = 10
c = 5
d = 1
coins = 0
# check the validity of input hight
while True:
    pass
    dollar = get_float("Change owed:")
    if dollar > 0:
        break
# convert dollars into pins
pins = round(100 * dollar, 2)
# check if pis is divisble by quarters
if pins % a == 0:
    print(pins/a)
    sys.exit()

while pins > a:
    coins += 1
    pins -= a

while pins >= b:
    coins += 1
    pins -= b

while pins >= c:
    coins += 1
    pins -= c

while pins >= d:
    coins += 1
    pins -= d
# print the minimum numbe number of coins
print(coins)