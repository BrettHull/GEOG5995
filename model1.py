#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 10:04:57 2019

@author: brett
"""

import random

y0 = random.randint(0,99)
x0 = random.randint(0,99)

print (y0,x0)


if random.random() < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1
        
    
if random.random() < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1        
        
print (y0,x0)

if random.random() < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1
        
    
if random.random() < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1        
        
print (y0,x0)

y1 = random.randint(0,99)
x1 = random.randint(0,99)

print (y1,x1)


if random.random() < 0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1
        
    
if random.random() < 0.5:
    x = x1 + 1
else:
    x1 = x1 - 1        
        
print (y1,x1)

if random.random() < 0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1
        
    
if random.random() < 0.5:
    x1 = x1 + 1
else:
    x1 = x1 - 1        
        
print (y1,x1)

answer = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5
print(answer)