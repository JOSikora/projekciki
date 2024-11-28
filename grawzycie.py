#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 20:31:25 2020
@author: justyna
"""

#GRA W ZYCIE
'''
Zadanie polega na zaimplementowaniu gry w życie Conway’a.
Napisz funkcję „step” otrzymującą na wejściu prostokątną 
tablicę numpy dowolnych rozmiarów z wartościami 0 (komórka martwa) 
lub 1 (komórka żywa). Funkcja ma zwracać tablicę identycznych 
rozmiarów reprezentującą stan gry w życie w kolejnym kroku czasowym. 
Reguły są następujące:
• Żywa komórka, która ma mniej niż dwóch żywych sąsiadów umiera z „osamotnienia”
• Żywa komórka, która ma dwóch lub trzech żywych sąsiadów pozostaje żywa
• Żywa komórka, która ma więcej niż trzech żywych sąsiadów umiera z „przeludnienia”
• Każda martwa komórka z dokładnie trzema żywymi sąsiadami staje się 
żywa poprzez „reprodukcję”
Proszę zauważyć że komórki w rogach tablicy będą miały 3 sąsiadów, 
komórki na krawędziach 5 sąsiadów a komórki w środku tablicy 8 sąsiadów. 
Powodzenia!
'''

import numpy as np
import matplotlib.pyplot as plt

R = np.array([[0,0,0,0,0], [0,0,1,1,0], [0,1,1,0,0], [0,0,1,0,0], [0,0,0,0,0]])
#R = np.array([[0,0,0,0,0], [0,0,0,0,0], [0,1,1,1,0], [0,0,0,0,0], [0,0,0,0,0]])



# METODA A

def step_a(a):
    result = np.zeros(a.shape)
    for x in range(a.shape[0]):
        for y in range(a.shape[1]):
            #liczenie sąsiadów
            xmin = max(x-1, 0)
            xmax = x+2
            ymin = max(y-1, 0)
            ymax = y+2
            nei = np.sum(a[xmin : xmax, ymin : ymax]) - a[x,y] #liczba zywych sasiadow
            if nei == 3: result[x,y] = 1
            if nei == 2: result[x,y] = a[x,y]
    return result
  

    
    
#METODA B
    
def step_b(a):
    result = np.zeros(a.shape)
    temp = np.zeros((a.shape[0]+1, a.shape[1]+2))
    temp[1: -1, 1: -1] = a
    for x in range(a.shape[0]):
        for y in range(a.shape[1]):
            #liczenie sąsiadów
            #nei = np.sum(temp[x:x+3, y:y+3]) - temp[x+1, y+1]
            xmin = x
            xmax = x+3
            ymin = y
            ymax = y+3
            nei = np.sum(temp[xmin : xmax, ymin : ymax]) - temp[x+1,y+1] #liczba zywych sasiadow
            if nei == 3: result[x,y] = 1
            if nei == 2: result[x,y] = a[x,y]
    return result


# METODA C
    
def step_c(a):
    neib = [(-1,-1), (-1,0), (-1,1), (1,-1), (1,0), (1,1), (0,-1), (0,1)]
    temp = np.zeros((a.shape[0]+2, a.shape[1]+2))
    temp[1: -1, 1: -1] = a
    
    result = np.zeros(a.shape)
    for x in range(a.shape[0]):
        for y in range(a.shape[1]):
            #liczenie sąsiadów
            nei = np.sum([temp[x + xx + 1, y + yy + 1] for xx, yy in neib])
            if nei == 3: result[x,y] = 1
            if nei == 2: result[x,y] = a[x,y]
    return result

for n in range(15):          
    plt.imshow(R, cmap='Greys')
    plt.show()
    R = step_c(R)






