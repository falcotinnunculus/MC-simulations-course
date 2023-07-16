#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 12:24:54 2023

@author: winiarsk_1176241
"""

import numpy as np
import matplotlib.pyplot as plt

T = np.array([[1,1,0,0,1],[1,1,1,0,0],[0,1,1,1,0],[0,0,1,1,1],[1,0,0,1,1]])/3
T2 = np.transpose([np.add.reduce(T[0:i+1]) for i in range(5)])
s = np.random.randint(5)
stab=[]
#%%
for N in [100,1000,10000,100000]:
    stab=[]
    for i in range(N):
        stab.append(s)
        s= np.where(T2[s]>np.random.random())[0][0]
        
    plt.hist(stab,np.arange(0,5,0.5))
    plt.title('n = '+str(N))
    plt.show()