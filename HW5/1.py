# -*- coding: utf-8 -*-
# @Author: Santosh
# @Date:   2018-03-03 18:55:59
# @Last Modified by:   Santosh
# @Last Modified time: 2018-03-03 19:13:28


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