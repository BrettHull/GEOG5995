#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 10:04:57 2019

@author: brett
"""
# Import statements
import random
import operator
import matplotlib.pyplot

# Create list of agents
agents = []
num_of_agents = 10
num_of_iterations = 100

# Create agents
for i in range (num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])

# Move agents
for j in range (num_of_iterations):
    for i in range(num_of_agents):    
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100
            
            
            
        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100      


# Calculate the distance between agents
def distance_between(agents_row_a, agents_row_b):
   return (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5

# Draw and print the graph
matplotlib.pyplot.ylim(0, 100)
matplotlib.pyplot.xlim(0, 100)

for i in range (num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
    
matplotlib.pyplot.show()
    
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
        print(distance)