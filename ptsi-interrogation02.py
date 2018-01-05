# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 16:25:23 2017

@author: eric
"""
def valeurnulle(L):
    reponse=-1
    n=len(L)
    for k in range(n):
        if L[k]==0:
            reponse=k
            return(reponse)
    return(reponse)

#print(valeurnulle([1,2,3,4,9]))

#print(valeurnulle([1,2,0,4,3]))

def listeIndice(L):
    n=len(L)
    reponse=[]
    for k in range(n):
        if L[k]==0:
            reponse.append(k)
    return(reponse)
    
#print(listeIndice([0,2,6,0]))
            
def minimum(L):
    n=len(L)
    minimum=L[0]
    position=0
    for k in range(1,n):
        if L[k]<minimum:
            minimum=L[k]
            position=k
    return(minimum,position)
            
#print(minimum([-1,0,10,4,-52,2,8,-52]))