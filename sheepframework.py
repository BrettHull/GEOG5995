#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 16:40:51 2019

__version__ 1.0.0
This is a framework for Sheep agents in the model. The sheep are given a position on a 2D plane and can move around
the area. 
"""

import random

class Sheep:
    
    def __init__(self, environment, sheep): 
    '''
    Initialises a Sheep.
    
    Positional arguements:
    environment - the environment to be shared with all agents
    sheep - a list of all Sheep agents
    x - the x axis coordinate for an agent
    y - the y axis coordinate for an agent 
    '''
        self._x = random.randint(0,300)
        self._y = random.randint(0,300)
        self.environment = environment
        self.store = 0
        self.sheep = sheep
        
    def move(self):
        '''
        Moves Sheep one step at random
        '''
        if random.random() < 0.5:
            self._y = (self._y + 1) % 300
        else:
            self._y = (self._y - 1) % 300

        if random.random() < 0.5:
            self._x = (self._x + 1) % 300
        else:
            self._x = (self._x - 1) % 300

    def eat(self): 
        '''
        Sheep eats 10 units of the environment and hold it in their store. 
        They will eat nothing if less than 10 units available.
        '''
        if self.environment[self._y][self._x] > 10:
           self.environment[self._y][self._x] -= 10
           self.store += 50
           return 0
        else:
           return 1
           
    def share_with_neighbours(self, neighbourhood):
    '''
    The distance between Sheep is calculated using the distance_between method. Any Sheep within a set neighbourhood of each other will 
    share their food with each other. Each share is based on the total contents of each Sheep's store divided by the number
    of sheep in the neighbourhood.
    
    Positional arguments: 
    neighbourhood - the distance within which the Sheep will share their store
    '''
        for agent in self.sheep:
            distance = self.distance_between(agent)
            if self != agent:
                if distance <= neighbourhood:
                    total = self.store + agent.store
                    average = total / 2
                    self.store = average
                    agent.store = average
    
    def distance_between(self, agent):
        '''
        Calculate the distance between self and agent(which at the moment will always be a Sheep)
        
        Positional arguments:
        agent - an agent to be compared against
        
        Returns:
        The distance between self and agent    
        '''
        return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5
    
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def set_x(self, x):
        self._x = x
        
    def set_y(self, y):
        self._y = y
        