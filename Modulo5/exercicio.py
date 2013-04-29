# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Documents and Settings\i12199\.spyder2\.temp.py
"""

a = [0]*10
for i in range(len(a)):
    a[i]=input("introduza numero")
        
soma=0.0
for i in range(len(a)):
    soma=soma+a[i]
print "Soma = ", soma
print "Media = ", soma/len(a)

    
maior = a[0]
for i in range(len(a)):
    if a[i]>maior:
        maior=a[i]
print "Maior = ", maior     