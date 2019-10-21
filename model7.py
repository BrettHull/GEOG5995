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
import agentframework7


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
neighbourhood = 20

# Create agents
for i in range (num_of_agents):
    agents.append(agentframework7.Agent(environment, agents))

# Move agents
for j in range (num_of_iterations):
    random.shuffle(agents)
    for i in range(num_of_agents):    
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)

# Clear previous plot
matplotlib.pyplot.clf()

# Draw and print the graph
matplotlib.pyplot.ylim(0, 300)
matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.imshow(environment)

for i in range (num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)

matplotlib.pyplot.show()



    