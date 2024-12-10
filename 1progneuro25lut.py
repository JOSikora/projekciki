#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 11:18:37 2020
@author: jo406066
"""
# zajecia1
# 25 lutego

#WARUNKI
x = 10

if x>0:
    a = 5
else:
    a = 10
    
#inna metoda  
a = 5 if x>0 else 10


#PĘTLE
x = 10

while True:
    print(x)    
    if x < 0: break
    x = x - 1
#out: 10 9 8 7 6 5 4 3 2 1 0 -1


mx = 100
s = 0
lista = [1,49,50,10]
i = 0

while s < mx:
    s += lista[i]
    i += 1
    print('s =', s, ' i =', i)
#out: s=1 i=1, s=50 i=2, s=100 i=3
    
tup = (1,2)
#a = tup[0]
#b = tup[1]
a,b = tup

lista = [(1,2), (49,100), (50,3), (10,4)]

for x,y in lista:
    n = x + y
    if n > 100: continue
    print(x,y)
#out: 1 2   ,    50 3   ,    10 4  
    
def fun(x):
    print(x**2)
    
b = fun(5) #nie zwraca nic, b to nic (output po wpisaniu b)
#out: 25

def funn(x):
    return(x**2)
    
c = funn(5) #zwraca 25 (output po wpisaniu b)
#out: "nic" bo returnuje a nie printuje


#PRZESTRZENIE NAZW
a = 1
b = 10

def fun1(x):
    global a
    a = 100
    b = x**2
    return a+b
print(fun1(5))
# out: 125


x = 6
def fun2(y):
    global x
    x += 1
    return x

print(fun2(x+1))
print(x)
#out: 7    7 
    

x = 6

def fun(x):
    x += 1
    def funn1(y):
        global x #używamy globalnego x i go zastępujemy 
        x += y
    funn1(x)
    return x

x = 7
print(fun(x))
print(x)
#out:8    15  (jest dobrze)
    
    
    
    
    
    
    
    
    
    
    