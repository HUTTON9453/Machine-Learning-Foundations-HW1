# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 21:27:18 2019

@author: hutton
"""

#
# Draw the Hoeffding's Inequality with the epsilons = 0.8 and the probability.
#

from scipy import signal
import numpy as np
import math

def hoeffding (x, epsilon):
    y = 2.0 * math.exp (-2*epsilon*epsilon*x)
    return y

x = np.arange (0, 20, 0.01)

y = [hoeffding (x, 0.8) for x in x]

import matplotlib.pyplot as plt

plt.xlabel ('N')
plt.ylabel ('P')
latex1 = r'P\leq2e^{\left( -2\varepsilon ^{2}N\right)}'
plt.title (r"Hoeffding's Inequality: $ %s $" % latex1)

latext2 = r'\varepsilon'
plt.plot (x, y, label='$%s$ = 0.8' % latext2)

x2 = 10
y2 = hoeffding (10, 0.8)
#plt.plot ([0, 10], [y2, y2], label='y = %f' % y2)
plt.axhline (y = y2, color='grey', linestyle='--')
plt.axvline (x = x2, color='grey', linestyle='--')
plt.scatter (x2, y2, color='red', label='x = %d, y = %f' % (x2, y2))

plt.legend ()
plt.show ()