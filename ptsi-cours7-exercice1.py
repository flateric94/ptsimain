# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 16:58:39 2017

@author: eric
"""

import matplotlib.pyplot as plt
import math as ma

N=1000
Listex=[k*4*ma.pi/N for k in range(N+1)]
Listeycos=[ma.cos(x) for x in Listex]
Listeysin=[ma.sin(x) for x in Listex]

plt.plot(Listex,Listeycos)
plt.show()
