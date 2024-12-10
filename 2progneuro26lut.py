#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 10:18:37 2020
@author: jo406066
"""
# zajecia2
# 26 lutego

a = [1,2,3]

def fun(lista):
    lista.append(4)
    lista = []
    lista.append(4)
    print(lista)
    
fun(a) #out: [4]
print(a) #out:[1,2,3,4]


a = [1,2,3,4,5]

b=[]
for x in a:
    b.append(x**2)
    
#inny sposób
c = [x**2 for x in a]

print(b) #out: [1, 4, 9, 16, 25]
print(c) #out: [1, 4, 9, 16, 25]


def fun(x):
    return x**2

fun1 = fun
print(fun1(5)) #out: 25

def fun(x, y = None):
    if y == None: y = []
    print('x =', x, 'y =', y)
    return x**2

print(fun(5)) # 5 to x
#out: x = 5 y = []       25


def fun(x, y = 10, z = 20):
    print('x =', x, 'y =', y, 'z =', z)

fun(5, z = 50) #nie pozwalamy na kontrowersje, najpierw bez nazwy, a potem z nazwą.
#out: x = 5 y = 10 z = 50


def sumuj(x, y = 5, *args):#bez tej gwiazdki by nie działało!!!
    print(x,y)
    print(args)
    
sumuj(1,2,3,4,5,6,7,8,9) # 1 to x, 2 to y, resta to args w postaci krotki
# 1 2   (3, 4, 5, 6, 7, 8, 9)


def sumuj(x, *args, y = 5):#bez tej gwiazdki by nie działało!!!
    print(x,y)
    print(args)
    
sumuj(1,2,3,4,5,6,7,8,9) # 1 to x, reszta to args w postaci krotki, oraz z funkcji y to 5
#out: 1 5    (2, 3, 4, 5, 6, 7, 8, 9)

def sumuj(**kwargs): #slownik
    print(kwargs)
    
sumuj(a=1, b=2, c=3) #out: {'a': 1, 'b': 2, 'c': 3}
sumuj(b=2, a=1, c=3) #out: {'b': 2, 'a': 1, 'c': 3}


def sumuj(*args, **kwargs): #krotka i slownik
    print(args)
    print(kwargs)
    
sumuj(5, 6, 7, a=1, b=2, c=3) #(5, 6, 7)   {'a': 1, 'b': 2, 'c': 3}
sumuj(6, 7, 8, b=2, a=1, c=3) #(6, 7, 8)   {'b': 2, 'a': 1, 'c': 3}


def sumuj(x, *args, **kwargs): #liczba, krotka i slownik
    print(x)
    print(args)
    print(kwargs)
    
sumuj(5, 6, 7, a=1, b=2, c=3) #out: 5    (6, 7)     {'a': 1, 'b': 2, 'c': 3}


def sumuj(x, y=1, *args, **kwargs): 
    print(x)
    print(y)
    print(args)
    print(kwargs)
    
sumuj(5, 6, 7, a=1, b=2, c=3) #out: 5  6  (7,)   {'a': 1, 'b': 2, 'c': 3}


def sumuj(x,  *args, y=1, **kwargs): 
    print(x)
    print(y)
    print(args)
    print(kwargs)
    
sumuj(5,6,7,a=1, b=2, c=3) #out: 5  1  (6, 7)  {'a': 1, 'b': 2, 'c': 3}


def sumuj(x,  *args, a=1,**kwargs): 
    print(x)
    print(a)
    print(args)
    print(kwargs)
    
#najpierw bez nazw a potem z nazwami    
sumuj(5,6,7,a=1, b=2, c=3) #out: 5  1  (6, 7)  {'b': 2, 'c': 3}
sumuj(6,7,8, b=2, a=10, c=3) #out: 6  10  (7, 8)  {'b': 2, 'c': 3}


def fun(x, y, z, a, b, c):
    print(x, y, z)
    print(a, b, c)
    
cc = ('ala', 'ma', 'kota', 1, 2, 3)

fun(cc[0], cc[1], cc[2], cc[3], cc[4], cc[5]) #out: ala ma kota 1 2 3
#fun(x, y, z, a, b, c=cc) tak jest ŻLE!!!
fun(*cc) #rozpakowuje nam krotkę, czyli out: ala ma kota 1 2 3
#PS z listami tez tak działa :)

#ze słownikami i dwiema gwiazdkami działa ten sam trik
dd = {'x':'ala', 'y':'ma', 'z':'kota', 'a':1, 'b':2, 'c':3}
fun(**dd) #out: ala ma kota 1 2 3


#PYTANIE KOLOKWIALNE
def task1(x, *args):
    return args

print(task1(1,2,3,4,5)) #out: (2,3,4,5)
print(task1(*task1(*task1(1,2,3,4,5)))) #out: (4,5)

#wycinki
a = [1,2,3,4,5]
print(len(a)) #out: 5
print(a[0]) #out: 1
print(a[-0]) #out: 1
print(a[0:3]) #out: [1, 2, 3]
print(a[-1]) #out: 5
print(a[1:-1]) #out: [2, 3, 4]
print(a[1:]) #out: [2, 3, 4, 5]
print(a[:-1]) #out: [1, 2, 3, 4] nie printuje mi ostatniej liczby z listy
print((a[:-1][:-1])) #out: [1, 2, 3] nie printuje mi dwóch ostatnich z listy
print(a[:-1][:-1][:-1]) #out: [1,2] nie printuje mi trzech ostatnich z listy


#PYTANIE KOLOKWIALNE
def task2(x, *args):
    return args[:-1]

print(task2(*task2(*task2(1,2,3,4,5,6,7,8,9)))) #out: (4, 5, 6)


a = [2,3,2,2,3,2,3,4,2,2]
b = [0,1,0,0,1,1,1,0,0,0]

def dis(fun, a, b):
    suma = 0
    for i in range(len(a)):
        suma += fun(a[i], b[i])
    return suma

#zamiast tworzyć osobną funkcję pomocniczą do tworzenia f kwadratowej, to robimy to
#w jedenj linijce dzięki lambda
#def sq(x,y):
#    return (x-y)**2

print(dis(lambda x,y: (x-y)**2, a, b)) #funkcja w jednek linijce dzięki lambda
#out: 49

#ZADANKA
'''Dokoncz linijke tak, by funkcja fun zliczala 
nieparzyste elementy (liczby) z listy otrzymanej jako argument'''

fun = lambda x: sum([y%2 for y in x])
print(fun(a)) #out: 3

'''Dokoncz linijke tak, by funkcja fun zliczala
sumę elementów większych niz 2 z listy otrzymanej jako argument'''

fun = lambda x: sum([y if y >2 else 0 for y in x])
print(fun(a)) #out: 13


def fun(x):
    l = []
    for i in range(len(x)):
        if x[i] > 2: l.append(x[i])
    return sum(l)
print(fun(a)) #out: 13
        

def rysunek(n):
    for i in range(n):
        print('a'*(i+1))
rysunek(5)
''' out:
a
aa
aaa
aaaa
aaaaa
'''

def rysunek(n):
    for i in range(n):
        print(' '*(n-i-1), 'a'*(i+1))
rysunek(5)
''' out:
     a
    aa
   aaa
  aaaa
 aaaaa
'''

def rysunek(n):
    for i in range(n):
        print(' '*(n-i-1), 'a'*(2*i+1))
rysunek(5)
''' out:
     a
    aaa
   aaaaa
  aaaaaaa
 aaaaaaaaa
'''

def rysunek(n):
    for i in range(n):
        print(' '*i, 'a')
rysunek(5)
''' out:
 a
  a
   a
    a
     a
'''

def rysunek(n):
    for i in range(n):
        print(' '*(n-i-1), 'a')
rysunek(5)
''' out:
     a
    a
   a
  a
 a
'''

def rysunek(n):
    for i in range(n):
        print(' '*i,'a',' '*(2*n-2*i-1),'a', sep='')

    print(' '*(n),'a',sep='')
    for i in range(n):
        print(' '*(n-i-1) , 'a', ' '*(2*i+1) , 'a', sep='')
rysunek(5)
''' out:
a         a
 a       a
  a     a
   a   a
    a a
     a
    a a
   a   a
  a     a
 a       a
a         a
'''




