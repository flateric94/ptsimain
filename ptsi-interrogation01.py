# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 15:49:07 2017

@author: eric
"""

def factorielle(n):
    Fact=1
    for k in range(1,n+1):
        Fact=Fact*k
    return(Fact)
    
#print(factorielle(5))

def Somme(p):
    u=0
    for k in range(0,p+1):
        u=u+(1/factorielle(k))
    return(u)
    
#print(Somme(3))

def u(n):
    u=1
    for k in range(1,n):
        u=((u+2)/k)
    return(u)

def sigmaU(n):
    s=0
    for k in range(n+1):
        s=s+u(k)
    return(s)
    
print(sigmaU(8000))
    
