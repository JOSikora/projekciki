#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 11:19:52 2020

@author: jo406066
"""

# zajęcia 3
# 3 marca

#funkcja rysująca kólko o promieniu r

def kolo(r):
    #2 ćw
    
    #1 ćw
    for  i in range(r-1,-1,-1):
        x = int(round((r*r-i*i)**0.5))
        print(' '*(r-x), '*' * 2*x)
    print
    #3 ćw
    #4 ćw
    for i in range(r):
        x = int(round((r*r-i*i)**0.5))
        print(' '*(r-x) , '*' * 2*x)
    
kolo(3)

#lepszy sposób
print('\n')
def kolko(r):
    n = int(round(r))
    for i in list(range(n-1, 0, -1)) + list(range(n)):
        x = int(round((r*r-i*i)**0.5))
        print((n-x)*' '+'*' *(2*x -1))
kolko(5)


#zadanko ćwiczące wszystko

def plot(fun, xmin, xmax, ymin, ymax):
    for i in range(ymax-ymin +1):
        l = []
        l.append([])     
        if i == 0: print(ymax, '|')
        elif i == ymax-ymin: print(ymin, ' |') #!!!!!!!!
        else: print(' '*2, '|')
        
        
        
    print(' '*2,'+'+'-'*(xmax-xmin+1))
    print(' '*3, xmin, ' '*(xmax-xmin-3), xmax)
        
 
    
    
plot(lambda x: x, 8, 15, 5, 10)

#lepszy sposób 


    

def plot(fun, xmin, xmax, ymin, ymax):
    a = [[' ' for x in range(xmax-xmin+1)] for x in range(ymax-ymin+1)]
    for x in range(xmin, xmax+1):
        y = int(round(fun(x)))
        if (y >= ymin) and (y <= ymax):
            a[y-ymin][x-xmin] = '*'
    for x in a[::-1]:
        print('|'+''.join(x))
    print('+'+'-'*(xmax-xmin+1))

import math

plot(lambda x: 5*math.sin(x/3), 0, 20, -5, 5)            
        

    
    
    
    
    
    
    
    
    
    
    
    
    



