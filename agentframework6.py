#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 16:40:51 2019

@author: brett
"""

import random

class Agent:
    
    def __init__(self):
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)
        
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
