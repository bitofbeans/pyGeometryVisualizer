import visvis as vv # Visualizer
from visvis.text import Label
import numpy as np # Math functions
import PySimpleGUI as sg # For GUI
import PyQt5 # Guarantee a backend is included
from threading import Thread # Running multiple functions

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

# ----- Functions --------- #
def createPlane(pos, scale, direction=0, rot=0): # Plane creator
    ## (Position, Scale, Rotation)
    scale = list(scale) 
    scale.append(0.1) # Thickness of plane
    # Create object
    if direction != (0,0,0) and direction != 0: # If rotation is customized
        obj = vv.solidBox(pos,scale,direction,rotation=rot)
        print(rot)
    else:
        obj = vv.solidBox(pos,scale,rotation=rot)
    objects.append(obj) # Add to color map list
    return obj # Return box object

def createColorMap(): # Add color map to all objects
  for obj in objects: # Add color map for all objects
      N = obj._vertices.shape[0] # get vertices
      obj.SetValues( np.linspace(0,1,N) ) # honestly no clue
      obj.colormap = vv.CM_JET # set colormap to rainbow

plane = createPlane((0, 0, 0), (6, 6)) # Create a plane
createColorMap() # Create color map

# --- Run Program ------------- #
app = vv.use() # Create app instance

def guiLoop(): # GUI loop
  points = {}
  ALPHABET = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
  idx = 0
  run = True
  while run:
        sg.theme('Dark Blue 3')  # set gui theme
        # Define layout
        layout = [
            [sg.Text('Add Objects                                            ', justification='center')],
            [
                sg.Button("Add Plane"), 
                sg.Text("Rotation"), 
                sg.Spin([x for x in range(181)],size=(3,1), key="planeRot"),
                # ------ #
                sg.Text("Direction(x,y,z)"), 
                sg.Spin([x for x in range(-1000,1000)],size=(2,1),key="planeDX", initial_value=0),
                sg.Spin([x for x in range(-1000,1000)],size=(2,1),key="planeDY", initial_value=0),
                sg.Spin([x for x in range(-1000,1000)],size=(2,1),key="planeDZ", initial_value=0),
                # ------ #
                sg.Text("Position(x,y,z)"), 
                sg.Spin([x for x in range(-1000,1000)],size=(2,1),key="planeX", initial_value=0),
                sg.Spin([x for x in range(-1000,1000)],size=(2,1),key="planeY", initial_value=0),
                sg.Spin([x for x in range(-1000,1000)],size=(2,1),key="planeZ", initial_value=0)
            ],
            [
                sg.Button("Add Point"), 
                sg.Text("x,y,z"), 
                sg.Spin([x for x in range(-1000,1000)],size=(3,1),key="pointX", initial_value=0),
                sg.Spin([x for x in range(-1000,1000)],size=(3,1),key="pointY", initial_value=0),
                sg.Spin([x for x in range(-1000,1000)],size=(3,1),key="pointZ", initial_value=0)
            ],
            [
                sg.Button("Add Line"), 
                sg.Text("2 Points"), 
                sg.Spin(points.keys(), size=(3,1),key="line1", initial_value="A"),
                sg.Spin(points.keys(), size=(3,1),key="line2", initial_value="B"),            ],
            
        ]

        window = sg.Window('Add Objects', layout) # Open window
        event, values = window.read() # Get inputs
        window.close() # Close window

        if event == "Add Plane":
            # Get values
            rot = values["planeRot"] 
            direction = values["planeDX"], values["planeDY"], values["planeDZ"]
            xx,yy,zz = values["planeX"], values["planeY"], values["planeZ"]
            xx,yy,zz = float(xx), float(yy), float(zz)
            # Create plane
            plane = createPlane((xx, yy, zz), (6, 6), direction, rot)
            
        elif event == "Add Point":
            xx,yy,zz = values["pointX"], values["pointY"], values["pointZ"] # Get values
            xx,yy,zz = float(xx), float(yy), float(zz)
            pointset = vv.Point(xx,yy,zz) # Create point from pos
            
            points[ALPHABET[idx]] = xx, yy, zz # Add to points list
    
            point = vv.plot(pointset, ms='.', mc='w', mw='9', ls='', mew=0 ) # Plot point
            point.alpha = 0.5 # Transparent
            txt = vv.Text(a, ALPHABET[idx], xx-0.08, yy, zz+0.15, color='w') # Add Text label
            idx += 1 # Increment Point num
            print(points)
        elif event == "Add Line":
            p1 = points[values["line1"]] # get point 1
            p2 = points[values["line2"]] # get point 2

            pp = vv.Pointset(3) # create 3d pointset
            pp.append(p1) # add point1
            pp.append(p2) # add point2

            line = vv.solidLine(pp, radius = 0.1) # create line
            N = line._vertices.shape[0] # get vertices
            line.SetValues( np.linspace(0,1,N) )
            line.colormap = vv.CM_HOT

        if event == sg.WIN_CLOSED or event == 'Exit':
            run = False # Exit condition

        createColorMap() # Add color map to new object

Thread(target = guiLoop).start() # start guiLoop thread
Thread(target = app.Run()).start() # start app loop 

