# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 00:36:36 2019

@author: hutton
"""

import sys
import numpy as np

def loaddat(fileName):
    dataSet = np.loadtxt(fileName)
    dataSet = np.pad(dataSet,((0, 0), (1, 0)), 'constant', constant_values=1)
    return dataSet
def signf(num):
    if num > 0:return 1
    else: return -1
def errorrate(weight, dataset):
    err = 0.0
    for i in range(dataset.shape[0]):
        if signf(np.dot(weight,dataset[i][0:5])) != dataset[i][5]: err = err + 1
    return err/dataset.shape[0]
    
def pocket(dataset, itertimes):
    i = 0
    curiter = 0
    pocketw = np.array([0, 0, 0, 0, 0])
    w = np.array([0, 0, 0, 0, 0])
    while curiter < itertimes:
        if dataset[i][5] != signf(np.dot(w,dataset[i][0:5])):
            w = w + dataset[i][5] * dataset[i][0:5]
            #Q18
            
            if errorrate(w, dataset) < errorrate(pocketw, dataset):
                pocketw = w
            
            #Q19
            #pocketw = w
            
            curiter = curiter + 1
            
        if i == dataset.shape[0] - 1: i = 0
        else: i = i + 1
    
    return pocketw
    
    
    
def main():
    argv = sys.argv
    trainfile = argv[1]
    testfile = argv[2]
    testerr = 0.0
    
    trainSet = loaddat(trainfile)
    testSet = loaddat(testfile)
    
    
    for i in range(2000):
        np.random.shuffle(trainSet)
        #Q20
        #pocketw = pocket(trainSet, 100)
        #Q18
        pocketw = pocket(trainSet, 50)
        testerr = testerr + errorrate(pocketw, testSet)
        print(str(i)+" th:",testerr)
    print(testerr/2000)
    
    
if __name__ == '__main__':  
    main()