# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 17:21:42 2020

@author: Johnny
"""


def gcd(a, b): 
  
    if (a == 0): 
        return b 
    return gcd(b % a, a) 
   
def phi(n): 
  
    result = 1
    for i in range(2, n): 
        if (gcd(i, n) == 1): 
            result+=1
    return result
max=0
for x in range(1,1000001):
    if x/phi(x) > max:
        max=x/phi(x)
print(max)