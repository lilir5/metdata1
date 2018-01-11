# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 14:42:08 2017

@author: lroohi
"""
import numpy as np
import math

logp=[]
B=-6300*np.log(1+(np.e**4))
print(B)
for i in range(0,6301):
    if i==0:
        logp.append(B)
    else:
        s=0
        for j in range(6301-i,6301):
            s=s+np.log(j)
        p=0    
        for k in range(1,6301):
            p=p+np.log(k)
        logp.append(s-p+(4*i)+B)
print(logp)        
            
        
        
def multinomial_log(N, logp):
    log_rand = -np.random.exponential(size=N)
    print(log_rand)
    logp_cuml = np.logaddexp.accumulate(np.hstack([[-np.inf], logp]))
    print(logp_cuml)
    logp_cuml -= logp_cuml[-1]
    print(logp_cuml)
    return np.histogram(log_rand, bins=logp_cuml)[0]

k=multinomial_log(1, logp)
print(k)

        
        
