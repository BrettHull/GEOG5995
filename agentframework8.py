#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 16:40:51 2019

@author: brett
"""

import random

class Agent:
    
    def __init__(self, environment, agents):
        self.x = random.randint(0,300)
        self.y = random.randint(0,300)
        self.environment = environment
        self.store = 0
        self.agents = agents
        
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
        if self.environment[self.y][self.x] > 50:
           self.environment[self.y][self.x] -= 50
           self.store += 50
           return 0
        else:
           return 1
           
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            distance = self.distance_between(agent)
            if self != agent:
                if distance <= neighbourhood:
                    total = self.store + agent.store
                    average = total / 2
                    self.store = average
                    agent.store = average
    
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5