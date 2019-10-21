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
import matplotlib.animation
import agentframework8


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

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# Create list of agents
agents = []
num_of_agents = 50
num_of_iterations = 1000
neighbourhood = 20

# Create agents
for i in range (num_of_agents):
    agents.append(agentframework8.Agent(environment, agents))

carry_on = True

def update(frame_number):

    fig.clear()
    global carry_on
    env_consump = 0
    
    # Move required number of steps
    #for j in range(num_of_iterations):
    if (carry_on):
         random.shuffle(agents)
         for i in range(num_of_agents):
            agents[i].move()
            env_consump += agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
            
            # Create chart 
    matplotlib.pyplot.ylim(0, 300)
    matplotlib.pyplot.xlim(0, 300)
    matplotlib.pyplot.imshow(environment)
    
    print("Env consump: %d " % env_consump)
    print("Agents: %d" % num_of_agents)
    
    if env_consump >= num_of_agents/2:
        carry_on = False
        
    
    # Plot points
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color="white")
        
def gen_function(b = [0]):
    a = 0
    global carry_on
    while (a < num_of_iterations) & (carry_on) :
        yield a			
        a = a + 1 
        print("Iteration: %d" % a)

animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=gen_function)    

matplotlib.pyplot.show()



    