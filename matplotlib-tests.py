## -- Geometry Visualizer -- ##
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

# --- Start Code --- #

point  = np.array([1, 2, 3])
normal = np.array([1, 1, 2])

point2 = np.array([10, 50, 50])

# a plane is a*x+b*y+c*z+d=0
# [a,b,c] is the normal. Thus, we have to calculate
# d and we're set
d = -point.dot(normal)

# create x,y
xx, yy = np.meshgrid(range(10), range(10))

# calculate corresponding z
z = (-normal[0] * xx - normal[1] * yy - d) * 1. /normal[2]

#Create the figure
fig = plt.figure()

# Add an axes
ax = fig.add_subplot(111,projection='3d')

# plot the surface
ax.plot_surface(xx, yy, z, alpha=0.8, cmap=cm.inferno)

# and plot the point 
ax.scatter(point2[0] , point2[1] , point2[2],  color='green')
# --- Render and Finish ---
plt.show()