#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 10:17:53 2020

@author: jo406066
"""

# zajecia 4
# 4 marca 

import numpy as np

#a = np.array(range(9)).shape((3,3))
#print(a)

#tak nie robimy
s = 0
#for i in range(a.shape[0]):
#    s += a[0,i]*a[1,i]
print(s)

#tak robimy
#print(np.dot(a[0,:], a[1,:]))


#KOLKO I KRZYZYK

#poczatek k i k
def zwracacz(a):
    if a == 0:
        return ' '
    if a == 1:
        return 'o'
    if a == 2: 
        return 'x'
    else:
        print('błąd')

plansza = np.zeros((5,5))
def rysuj(plansza):
    d = len(plansza[0,:])
    for i in range(d):
        if i != d - 1:
            print('   |'*(d-1))
            print('---+'*d)
        else:
            print('   |'*(d-1))
            
rysuj(plansza)
print('\n')




#schemat gry

#vec to jednowymiarowa tablica (wektor)
def sprawdz_linie(vec):
    #gdy vec ma same jedynki zwraca 1
    #gdy vec ma same dwojki zwraca 2
    #w pozostalych przypadkach zwraca 0
    



i = 1
while (len(plansza.flatten()) - np.count_nonzero(plansza)):
    
    #rysujemy plansze
    rysuj(plansza)
    
    #ruch gracza i
    while True:
        'podaj wspolrzedne x,y'
        if (plansza[x,y] == 0): break
    plansza[x,y] == i
    
    #rysujemy plansze
    rysuj(plansza)
    
    #zmieniamy gracza
    i = 1+ i%2
    
print('KONIEC GRY')




#moje nieudolne próby
def rysuj(plansza):
    kreska = ('---+'*plansza.shape[1])[:-1]
    def znak(z):
        if z == 1:
            return ' o '
        if z == 2: 
            return ' x '
        return '   '
    for i in range(plansza.shape[0]):
        print('|'.join([znak(liczba) for liczba in plansza[i,:]]))
        if (i<plansza.shape[0] - 1): print(kreska)
        
for k in range(9):
    ox = int(input('Graczu 1, podaj po przecinku wspołrzedną x kólka:'))
    oy = int(input('Graczu 1, podaj po przecinku wspołrzedną y kólka:'))
    if plansza[ox, oy] == 0:
        print(' to pole jest zajęte')
        while 
    else:
        plansza[ox,oy] = 1
    rysuj(plansza)
    xx = int(input('Graczu 2, podaj po przecinku współrzędną x krzyżyka:'))
    xy = int(input('Graczu 2, podaj po przecinku współrzędną y krzyżyka:'))
    plansza[xx, xy] = 2
    rysuj(plansza)
        
rysuj(plansza)



















