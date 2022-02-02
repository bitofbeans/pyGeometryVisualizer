import visvis as vv # Visualizer
from visvis.text import Label
import numpy as np # Math functions
import PySimpleGUI as sg # For GUI
import PyQt5 # Guarantee a backend is included
from threading import Thread # Running multiple functions
from func import createColorMap, createPlane
from gui import guiLoop

# ----- Setup VisVis ----- #
fig = vv.figure() # Create figure
fig.position.w = 700 # Resize window width
fig.position.h = 500 # Resize window height

vv.xlabel('x axis') # Set axis label
vv.ylabel('y axis') # Set axis label
vv.zlabel('z axis') # Set axis label

a = vv.subplot(111) # Create axes
a.bgcolor = 'k'
a.axis.axisColor = 'w'
a.axis.showGrid = 1

objects = [] # List of all objects for color map

# --- Create default plane ---- #
plane = createPlane(objects,(0, 0, 0), (6, 6)) # Create a plane
createColorMap(objects) # Create color map

# --- Run Program ------------- #
app = vv.use() # Create app instance

Thread(target = guiLoop(a,objects)).start() # start guiLoop thread
Thread(target = app.Run()).start() # start app loop 

