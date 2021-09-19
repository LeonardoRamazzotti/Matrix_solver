#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 00:25:34 2021

@author: leonardo
"""

# funzione che mi crea una lista di n tuple , dove n e' il nunmero di valori della matrice
# nella tutpla avro' riga e colonna (riga,colonna)


from tkinter import *


root = Tk()
root.geometry('1080x720')


def grid_tuple(n):  # function that create a list of tuple for the grid layout (row,column)

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

    return lista_tuple
     
def list_matrix(num):
    
    list_a =[]
    
    i=0
    while i < num:
        list_a.append(i)
        i+=1
        
        
    return list_a
    
n=16
row =4

list_grid= grid_tuple(row)

list_val = list_matrix(n)

i=0

for element in list_val :
   
    r = list_grid[i][0]
    col = list_grid[i][1]    
         
    c = str(i)
    
    globals()['Entry_'+c]= Entry(root,width=10).grid(row=r,column =col,padx=20,pady=20)
    
    i+=1
    
root.mainloop()
    