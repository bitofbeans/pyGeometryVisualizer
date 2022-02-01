import visvis as vv # Visualizer
import numpy as np # Math functions
import PySimpleGUI as sg # For GUI

# --- Start Code  --- #

fig = vv.figure() # Create figure
fig.position.w = 700 # Resize window width
fig.position.h = 500 # Resize window height

a = vv.subplot(111) # Create axes

objects = [] # List of all objects for color map

# Plane creator
def createPlane(pos, scale, rot=0):
    scale = list(scale) 
    scale.append(0.1) # Thickness of plane
    # Create object
    if rot: # If rotation is customized
        obj = vv.solidBox(pos,scale,rot)
    else:
        obj = vv.solidBox(pos,scale)
    objects.append(obj) # Add to color map list
    return obj # Return box object
     
# Create plane
 ## (Position, Scale, Rotation)
plane = createPlane((0, 0, 0), (6, 6))
plane2 = createPlane((0, 0, 1), (6, 6), (0,1,0))

for obj in objects: # Add color map for all objects
    N = obj._vertices.shape[0] # get vertices
    obj.SetValues( np.linspace(0,1,N) ) # honestly no clue
    obj.colormap = vv.CM_JET # set colormap to rainbow

# --- Run Program --- #
app = vv.use() # Create app instance

## We don't need an app.Run() 
## in this because our GUI
## is acting as the loop

# GUI loop
run = True
while run:
    sg.theme('Dark Blue 3')  # set gui theme
    # Define layout
    layout = [
        [sg.Text('Add Objects                                            ', justification='center')],
        [sg.Button("Add Plane")],
        [sg.Button("Add Plane")],
    ]
    window = sg.Window('Add Objects', layout) # Open window
    event, values = window.read() # Get inputs
    window.close() # Close window
    
    if event == sg.WIN_CLOSED or event == 'Exit':
        run = False # Exit condition
