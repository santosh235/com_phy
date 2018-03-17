# -*- coding: utf-8 -*-
# @Author: santosh
# @Date:   2018-03-17 16:41:48
# @Last Modified by:   santosh


""" A random point on surface of the Earth"""

import random
from math import acos,pi

z = random.random()

phi = 2*pi*z
theta = acos(1 - 2*z)

print('phi(radian) = %f' %(phi))
print('theta(radian)  = %f' %(theta))