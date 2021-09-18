#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 00:25:34 2021

@author: leonardo
"""

# funzione che mi crea una lista di n tuple , dove n e' il nunmero di valori della matrice
# nella tutpla avro' riga e colonna (riga,colonna)



n= 4

c = 0 

lista_tuple = []

while c < n :
     m=0
     while m < n:
         tupla = (c,m)
         lista_tuple.append(tupla)
         m+=1
     m =0
     c+=1
     
     
    