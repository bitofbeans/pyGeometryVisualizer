import visvis as vv # Visualizer
import numpy as np # Math functions

# ----- Functions --------- #
def createPlane(objects, pos, scale, direction=0, rot=0): # Plane creator
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

def createColorMap(objects): # Add color map to all objects
  for obj in objects: # Add color map for all objects
      N = obj._vertices.shape[0] # get vertices
      obj.SetValues( np.linspace(0,1,N) ) # honestly no clue
      obj.colormap = vv.CM_JET # set colormap to rainbow
