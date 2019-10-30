#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 18:28:00 2019

__version__ 1.0.0
This is a framework for Wolf agents in the model. The wolves are given a position on a 2D plane and are static. They will
eat any sheep which come within their neighbourhood
"""

import random


class Wolf:
    
    def __init__(self, environment, sheep):
        '''
    Initialises a Wolf.
    
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

    def eat(self, s): 
                '''
        Wolf eats a sheep gaining 100 units plus the contents of the sheep's store hold it in their store. 
        They will eat nothing if there are no sheep in the neighbourhood.
        
        Positional arguements:
        s - the Sheep which is eaten
        '''
        self.store += 100 + s.store
        self.sheep.remove(s)
        
       
    def check_neighbourhood(self, neighbourhood):
        '''
        Checks the neighbourhood of the Wolf
        
        Positional arguements:
        neighbourhood - the distance within which a Wolf will eat a Sheep
        
        Returns:
        sheep_eaten: the number of sheep which are eaten by a Wolf in an iteration
        '''
        sheep_eaten = 0
        for s in self.sheep:
            distance = self.distance_between(s)
            if distance <= neighbourhood:
                self.eat(s)
                sheep_eaten += 1
        return sheep_eaten
            
           
    def distance_between(self, agent):
        '''
        Calculate the distance between self and agent(which at the moment will always be a Sheep)
        
        Positional arguments:
        agent - an agent to be compared against
        
        Returns:
        The distance between self and agent    
        '''
        return (((self._x - agent.get_x())**2) + ((self._y - agent.get_y())**2))**0.5
    
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def set_x(self, x):
        self._x = x
        
    def set_y(self, y):
        self._y = y