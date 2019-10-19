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

# Add first agent to list
agents.append([random.randint(0,99),random.randint(0,99)])

print (agents)
# Move agent two steps
if random.random() < 0.5:
    agents[0][0] = agents[0][0] + 1
else:
    agents[0][0] = agents[0][0] - 1
        
if random.random() < 0.5:
    agents[0][1] = agents[0][1] + 1
else:
    agents[0][1] = agents[0][1] - 1        
        
print (agents)


if random.random() < 0.5:
    agents[0][0] = agents[0][0] + 1
else:
    agents[0][0] = agents[0][0] - 1
        
    
if random.random() < 0.5:
    agents[0][1] = agents[0][1] + 1
else:
    agents[0][1] = agents[0][1] - 1        
        
print (agents)


# Add second agent to list
agents.append([random.randint(0,99),random.randint(0,99)])

print (agents)

# Move second agent two steps
if random.random() < 0.5:
    agents[1][0] = agents[1][0] + 1
else:
    agents[1][0] = agents[1][0] - 1
        
    
if random.random() < 0.5:
    agents[1][1] = agents[1][1] + 1
else:
    agents[1][1] = agents[1][1] - 1        
        
print (agents)

if random.random() < 0.5:
    agents[1][0] = agents[1][0] + 1
else:
    agents[1][0] = agents[1][0] - 1
        
    
if random.random() < 0.5:
    agents[1][1] = agents[1][1] + 1
else:
    agents[1][1] = agents[1][1] - 1        
        
print (agents)


# Calculate the distance between agents
answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
print(answer)

print(max(agents, key=operator.itemgetter(1)))

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
eastern = max(agents, key=operator.itemgetter(1))
matplotlib.pyplot.scatter(eastern[1], eastern[0], color='red')

matplotlib.pyplot.draw()