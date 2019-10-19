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

for i in range (num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])

print (agents)

for i in range (num_of_iterations):
    for i in range(num_of_agents):    
        print (agents[i])
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100
            
            
            
        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100      


# Calculate the distance between agents
'''answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
print(answer)

print(max(agents, key=operator.itemgetter(1)))'''

# Draw and print the graph
matplotlib.pyplot.ylim(0, 100)
matplotlib.pyplot.xlim(0, 100)

for i in range (num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
    matplotlib.pyplot.show()