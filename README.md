# GEOG5995
 Assignment 1 of GEOG 5995 - An agency based model of sheep in a field with hidden wolves
 
 ### About
 
This project takes a raster input file to create an environment which is placed into a 300 x 300 grid. This grid is populated with sheep that slowly eat the environment (grass) and wolves which eat the sheep if they come too close! The numbers of sheep, wolves, iterations, and proximities for the agents to eat are all configurable. The program outputs a live feed of the consequences of each iteration and all of the action is animated into a pop up window. Both the environment and iteration details are output to separate text files upon closing the model.

### Installation

You can install this model by navigating to the relevant github repository at https://github.com/BrettHull/GEOG5995 

### Running the model

Once installed, you can use the command line to navigate to the relevant folder and use the following command: 

python model10.py -i {input file for environment} -oe {output file for environment} -ol {output file for iterations} -ns {number of sheep wanted} -nw {number of wolves wanted} -ni {number of iterations} -nhs {neighbourhood size for sheep} -nhw {neighbour hood size for wolves}

Please note that the items inside the curly braces should be replaced with the relevant file names or integers wanted.

Default options are as follows:

-i = in.txt
-oe = out_env.txt
-ol = out_iterations.txt
-ns = 100
-nw = 10
-ni = 100
-nhs = 20
-nhw = 20

Any parameters not entered will revert to defaults and validation will be ran. 

Please note that the current model does not allow users to modify how much each sheep eats or the value of sheep to a wolf.

### License 

Please find the license at https://github.com/BrettHull/GEOG5995 

### Authors and acknowledgement

This work has been completed by Brett Hull and will be assessed towards completion of the GEOG5995 module. It has used and modified code taken from the practicals taught in the module which can be found at https://www.geog.leeds.ac.uk/courses/computing/study/core-python-phd/
