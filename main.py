import visvis as vv # visualizing
import numpy as np # math

# --- Start Code  --- #

# List of all objects for color map
objects = []

# plane creator
def createPlane(pos, scale):
    # Thickness of \/
    scale = list(scale)
    scale.append(0.25)
    # Create object
    obj = vv.solidBox(pos,scale)
    # Add to color map list
    objects.append(obj)
    # Return box object
    return obj
    
# Create plane
plane = createPlane((0, 0, 0), (6, 6))
plane2 = createPlane((0, 0, 1), (6, 6))



# Add color map for all objects
for obj in objects:
    # Set Color Map
    N = obj._vertices.shape[0]
    obj.SetValues( np.linspace(0,1,N) )
    obj.colormap = vv.CM_JET


# --- Run Program --- #
# Create axes
a = vv.gca()
a.camera = 3 # 1 = Fly, 2 = 2D, 3 = 3D

vv.title('Visualizer') # Set title
app = vv.use() # Create app instance
app.Run() # Run main loop
