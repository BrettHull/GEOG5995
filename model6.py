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
import agentframework6

# Calculate the distance between agents
def distance_between(agents_row_a, agents_row_b):
   return (((agents_row_a.x - agents_row_b.x)**2) + ((agents_row_a.y - agents_row_b.y)**2))**0.5

# Reads input file and generates the environment
f = open("in.txt")
environment = []
for line in f:
    parsed_line = str.split(line,",")
    rowlist = []
    for value in parsed_line:
        rowlist.append(float(value))
    environment.append(rowlist)
print(environment)
f.close()

# Create list of agents
agents = []
num_of_agents = 10
num_of_iterations = 100

# Create agents
for i in range (num_of_agents):
    agents.append(agentframework6.Agent())

# Move agents
for j in range (num_of_iterations):
    for i in range(num_of_agents):    
        agents[i].move()

# Draw and print the graph
matplotlib.pyplot.ylim(0, 100)
matplotlib.pyplot.xlim(0, 100)

for i in range (num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
    
matplotlib.pyplot.show()
    
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
                    
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()

