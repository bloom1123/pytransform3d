"""
==========================
Visualize Coordinate Frame
==========================
"""
print(__doc__)


import numpy as np
import pytransform3d.visualizer as pv


fig = pv.figure()
fig.plot_basis(R=np.eye(3), p=[0.1, 0.2, 0.3])
fig.view_init(azim=15, elev=30)
if "__file__" in globals():
    fig.show()
else:
    fig.save_image("__open3d_rendered_image.jpg")