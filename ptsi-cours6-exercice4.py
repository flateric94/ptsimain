# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 14:20:24 2017

@author: eric
"""

def sommation(L):
    S=0
    n=len(L)
    for k in range(n):
        S=S+L[k]
    return(S)
    
def sommationWhile(L):
    S=0
    n=len(L)
    k=0
    while k<n:
        S=S+L[k]
        k=k+1
    return(S)
    

print(sommation([1,2,3,4]))
print(sommationWhile([1,2,3,4]))

