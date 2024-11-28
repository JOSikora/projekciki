#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 20:01:01 2020

@author: justyna
"""

import numpy as np


plansza = np.zeros((3,3))
11
def rysuj(plansza):
    kreska = ('---+'*plansza.shape[1])[:-1]
    def znak(z):
        if z == 1: return ' O '
        if z == 2: return ' X '
        return '   '
    for i in range(plansza.shape[0]):
        print('|'.join([znak(liczba) for liczba in plansza[i,:]]))
        if (i<plansza.shape[0]-1): print(kreska)




#vec to jednowymiarowa tablica
def sprawdz_linie(vec):
    #gdy vec ma same jedynki zwraca 1
    #gdy vec ma same dwojki zwraca 2
    # w pozostałych przypadkach zwraca 0
    for i in [1,2]:
        if np.count_nonzero(vec-i) == 0: return i
    return 0
 
 
i=1
while True:
    #rysujemy plansze
    rysuj(plansza)
 
    #ruch gracza i
    while True:
        x = int(input('graczu '+str(i)+' podaj wspolrzedna x:'))
        y = int(input('graczu '+str(i)+' podaj wspolrzedna y:'))
        if (plansza[x,y] == 0): break
    plansza[x,y] = i
 
    if (len(plansza.flatten())-np.count_nonzero(plansza)) == 0:
        print('REMIS')
        break
 
    wyniki=[]
    for j in range(len(plansza)):
        wyniki.append(sprawdz_linie(plansza[j,:]))
        wyniki.append(sprawdz_linie(plansza[:,j]))
    wyniki.append(sprawdz_linie(np.diag(plansza)))
    wyniki.append(sprawdz_linie(np.diag(plansza[:,::-1])))
 
    wynik=max(wyniki)
    if wynik:
        print('wygral gracz '+str(wynik))
        break
 
    #zmien gracza
    i = 1 + i%2