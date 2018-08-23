#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 14:20:11 2018

@author: monestarazi
"""
global rand

def cong_random(iteration,index):
    rand = []
    x_value = 2**20         # Our seed, or X_0 = 123456789
    a = 22695477            # Our "a" base value
    b = 1                   # Our "b" base value
    m = (2**32)             # Our "m" base value 
    for i in range (iteration):
        
        x_value = (a * x_value + b) % m
        
        if x_value <= 2**31 :
            Comp_rand= 0
        else:
            Comp_rand= 1
            
        rand.append(Comp_rand)
        
       
    return rand[index]


     




