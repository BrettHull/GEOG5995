#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 16:40:51 2019

@author: brett
"""

import random

class Agent:
    
    def __init__(self, environment):
        self.x = random.randint(0,300)
        self.y = random.randint(0,300)
        self.environment = environment
        self.store = 0
        
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 300
        else:
            self.y = (self.y - 1) % 300

        if random.random() < 0.5:
            self.x = (self.x + 1) % 300
        else:
            self.x = (self.x - 1) % 300

    def eat(self): 
        if self.environment[self.y][self.x] > 10:
           self.environment[self.y][self.x] -= 10
           self.store += 10