# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 14:35:53 2017

@author: eric
"""

def valeurnulle(L):
    n=len(L)
    reponse=False
    for k in range(n):
        if L[k]==0:
            reponse=True
            return(reponse)
    return(reponse)
        
print(valeurnulle([1,0,8,6,2]))
print(valeurnulle([1,9,8,6,2]))


def valeurnulleWhile(L):
    n=len(L)
    reponse=False
    k=0
    while k<n:
        if L[k]==0:
            reponse=True
            return(reponse)
        k=k+1
    return(reponse)

print(valeurnulleWhile([1,0,8,6,2]))
print(valeurnulleWhile([1,9,8,6,2]))
    