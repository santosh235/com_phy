# -*- coding: utf-8 -*-
# @Author: santosh
# @Date:   2018-03-15 23:55:34
# @Last Modified by:   santosh


""" Random Number generator"""

import random

print("Dice 1: %d" %(random.randint(1,6)))
print("Dice 1: %d" %(random.randint(1,6)))


count = 0

# <ROLLING> THE DICE 1 MILLION TIMES
for x in range(1000000):
  d1 = random.randint(1,6)
  d2 = random.randint(1,6)

  if d1 == 6 and d2 == 6:
  	count = count + 1				#COUNT IS REGISTERED FOR EVERY DOUBLE SIX


#CALCULATING THE PROBABILITY OF DOUBLE SIX
prob = float(count / 1e6)
print("The probability of double six for 1 million events is : %f" %(prob))

