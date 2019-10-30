#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 10:04:57 2019

__version__ 1.0.0
This model is run from a GUI which is a drop down menu which has an option to run the model. When you run
this code, a window should appear on your screen. To run the model, find the model window and select run 
from the drop down menu.

"""

# Import statements
import matplotlib
matplotlib.use('TkAgg')
import random
import operator
import matplotlib.pyplot
import matplotlib.animation
import sheepframework
import wolfframework
import tkinter
import argparse

# Methods to be called
def run():
    '''
    Runs the model and continues to do so until a stopping criteria is met
    '''
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()

def update(frame_number):
    '''
    Updates the animation for each iteration
    '''
    fig.clear()
    global carry_on
    global num_of_sheep
    global f_it
    num_sheep_had_eaten = 0
    sheep_consumed = 0
    
    f_it.write(str(num_of_sheep) + ",")
    f_it.write(str(num_of_wolves) + ",")
    
    # Iterates the model and calls the eat and move methods from sheepframework.py
    if (carry_on):
        random.shuffle(sheep)
        for i in range(num_of_sheep):
            sheep[i].move()
            num_sheep_had_eaten += sheep[i].eat()
            sheep[i].share_with_neighbours(neighbourhood_sheep)
            
        # iterates the model and calls the eat method from wolfframework.py    
        for j in range (num_of_wolves):
            sheep_consumed_by_wolf = wolves[j].check_neighbourhood(neighbourhood_wolves)
            print("Sheep eaten by wolf %d : %d" % (j, sheep_consumed_by_wolf))
            f_it.write(str(sheep_consumed_by_wolf)+",")
            sheep_consumed += sheep_consumed_by_wolf
        num_of_sheep -= sheep_consumed
        num_sheep_had_eaten += sheep_consumed
                
    # Create chart 
    matplotlib.pyplot.ylim(0, 300)
    matplotlib.pyplot.xlim(0, 300)
    matplotlib.pyplot.imshow(environment)
    
    # Plot points
    for i in range(num_of_sheep):
            matplotlib.pyplot.scatter(sheep[i].get_x(), sheep[i].get_y(), color="white")
            
    for i in range(num_of_wolves):
            matplotlib.pyplot.scatter(wolves[i].get_x(), wolves[i].get_y(), color="black")        
        
    # Prints statistics to screen 
    print("Num sheep have not eaten: %d" % num_sheep_had_eaten)
    print("Sheep consumed: %d " % sheep_consumed)
    print("Sheep: %d" % num_of_sheep)
    print("Wolves: %d" % num_of_wolves)
    f_it.write(str(num_sheep_had_eaten) + ",")
    f_it.write(str(sheep_consumed) + "\n")
    
    # Tests to see if less than half of the sheep ate during the last iteration and stops the program if true
    if num_sheep_had_eaten > (num_of_sheep/2):
        carry_on = False
            
def gen_function(b = [0]): 
'''
This function creates a stopping criteria for the model
'''
    a = 0
    global carry_on
    while (a < num_of_iterations) & (carry_on) :     
        print("Iteration: %d" % a)
        f_it.write(str(a)+",")
        yield a			
        a = a + 1 
        
def exiting():
    '''
    Closes the model and creates outputs to be written to chosen files
    '''
    global f_it
    f_it.close()
    with open(outputfile_env, 'w') as f:
        for e in environment:
            f.write(",".join(str(x) for x in e)+"\n")
    root.quit()
    root.destroy()
    
'''
Main - creates the model and calls relevant methods
'''    

# Creates a parser to read arguments from command line    
parser = argparse.ArgumentParser()
parser.add_argument("-i", default = "in.txt", type = str, help = "This is the input file with the environment")
parser.add_argument("-oe", default = "out_env.txt", type = str, help = "This is the output file with the final environment")
parser.add_argument("-oi", default = "out_iterations.txt", type = str, help = "This is the output file with the iterations information")
parser.add_argument("-ns", default = 100, type = int, help = "This is the number of sheep variable")
parser.add_argument("-nw", default = 10, type = int, help = "This is the number of wolves variable")
parser.add_argument("-ni", default = 100, type = int, help = "This is the number of iterations variable")
parser.add_argument("-nhs", default = 20, type = int, help = "This is the neighbourhood size for sheep variable")
parser.add_argument("-nhw", default = 20, type = int, help = "This is the neighbourhood size for wolves variable")
args = parser.parse_args()
inputfile = args.i
outputfile_env = args.oe
outputfile_it = args.oi

# Reads input file and generates the environment
f = open(inputfile)
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

# Create list of agents and variables to store model parameters
sheep = []
wolves = []
num_of_sheep = args.ns
num_of_wolves = args.nw
num_of_iterations = args.ni
neighbourhood_sheep = args.nhs
neighbourhood_wolves = args.nhw

f_it = open(outputfile_it, "w")
f_it.write("Iteration,Initial_Num_Sheep,Number_Wolves")

# Create agents
for i in range (num_of_sheep):
    sheep.append(sheepframework.Sheep(environment, sheep))
    
for i in range (num_of_wolves):
    wolves.append(wolfframework.Wolf(environment, sheep))
    f_it.write(",Sheep_Eaten_By_Wolf_" + str(i))

f_it.write(",Num_Sheep_Have_Not_Eaten,Num_Sheep_Eaten\n")

carry_on = True

# Creates GUI drop down menu
root = tkinter.Tk() 
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu_bar =tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 

# Calls exit function to properly close model
root.protocol("WM_DELETE_WINDOW", exiting)

tkinter.mainloop()



