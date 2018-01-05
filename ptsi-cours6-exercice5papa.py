# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 14:54:11 2017

@author: eric
"""



L=[1,3,0,3,0,2,5,9,9,0]

def nombredetermes(x):
    n=len(L)
    nombre=0
    for k in range(n):
        if L[k]==x:
            nombre=nombre+1
    return(nombre)
    
def nbrdetermesW(x):
    n=len(L)
    nombre=0
    k=0
    while k<n:
        if L[k]==x:
            nombre=nombre+1
        k=k+1
    return(nombre)



print(nbrdetermesW(0))
print(nbrdetermesW(9))
print(nbrdetermesW(4))


#print(nombredetermes(0))
#print(nombredetermes(9))
