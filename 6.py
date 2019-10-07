# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 02:03:46 2019

@author: hutton
"""

import sys
import numpy as np
from matplotlib import pyplot as plt 
def loaddat(fileName):
    dataSet = np.loadtxt(fileName)
    dataSet = np.pad(dataSet,((0, 0), (1, 0)), 'constant', constant_values=1)
    return dataSet
def signf(num):
    if num > 0:return 1
    else: return -1
def PLA(dataset):
    cycle = 0
    i = 0
    updates = 0
    w = np.array([0, 0, 0, 0, 0])
    while cycle != dataset.shape[0]:

        if dataset[i][5] == signf(np.dot(w,dataset[i][0:5])): cycle = cycle + 1
        else:
            w = w + dataset[i][5] * dataset[i][0:5]
            updates = updates + 1
            cycle = 0
        if i == dataset.shape[0] - 1: i = 0
        else: i = i + 1
    
    return updates
    
    
    
def main():
    argv = sys.argv
    file = argv[1]
    updatesSum = 0
    updatesSeq = np.array([])
    
    dataSet = loaddat(file)
    
    for i in range(1126):
        np.random.shuffle(dataSet)
        updates = PLA(dataSet)
        updatesSum += updates
        updatesSeq = np.append(updatesSeq, updates)
    plt.hist(updatesSeq)
    plt.title("histogram") 
    print("the average number of updates:",updatesSum/1126)
    
    
if __name__ == '__main__':  
    main()