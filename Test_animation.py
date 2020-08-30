# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 02:59:39 2020

@author: Achraf
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import Curve_gradient_descent as gd 
import shapely.geometry as geom
import Curve_utils
import random
import geopandas as gpd
import Test as tst
import pandas as pd

# Set up the curve whose flow we will animate

############ Donnees importees  
cur = pd.read_json('circonscriptions-occitanie.json')
cur_fd = cur['fields']
#cur_fd[5]['geo_shape']['coordinates'][0]
a = np.array(cur_fd[5]['geo_shape']['coordinates'][0]) 
b = np.array(cur_fd[12]['geo_shape']['coordinates'][0]) 
curve = b
############

pp_data = np.empty((0,2), float)
# pt = np.array([0.0,0.0])
# curve = np.array([pt])
# for i in range(250):
# 	pt += np.array([random.uniform(-0.5,0.5), random.uniform(-0.5,0.5)])
# 	curve = np.append(curve, [pt], axis=0)

# curve = np.array([[np.cos(theta), np.sin(theta) - 4] for theta in np.linspace(1.5 * np.pi, 2 * np.pi, 5, endpoint=False)])

# Finally set up the figure, the axis, and the plot element we want to animate
# fig = plt.figure(figsize=(6,6))
fig, (ax1, ax2) = plt.subplots(1,2, figsize=(12,6)) 

######## MANUAL CONFIG #########
"""
#float au lieu de int pour avoir plus de versatilité
# ax1 = plt.axes(xlim=(-4, 4), ylim=(-4, 4))
minx1 = float(input('limite inf de l axe x1: '))
maxx1 = float(input('limite sup de l axe x1: '))
miny1 = float(input('limite inf de l axe y1: '))
maxy1 = float(input('limite sup de l axe y1: '))
minx2 = float(input('limite inf de l axe x2: '))
maxx2 = float(input('limite sup de l axe x2: '))
miny2 = float(input('limite inf de l axe y2: '))
maxy2 = float(input('limite sup de l axe y2: '))
"""

minx1 = min(curve[:,0])
maxx1 = max(curve[:,0])
miny1 = min(curve[:,1])
maxy1 = max(curve[:,1])
minx2 = 0
maxx2 = 50
miny2 = 0
maxy2 = 0.8



ax1.set_xlim(minx1,maxx1)
ax1.set_ylim(miny1,maxy1)
ax2.set_xlim(minx2,maxx2)
ax2.set_ylim(miny2,maxy2)
ax2.set_xlabel("Steps in flow")
ax2.set_ylabel("Polsby-Popper score")
line1, = ax1.plot([], [])
line2, = ax2.plot([], [])

pp_score = ax1.text(0.02, .9, '', transform=ax1.transAxes)
# step_num = ax1.text(0.02, .5, '', transform=ax1.transAxes)
plt.plot([], [])


# initialization function: plot the background of each frame
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    pp_score.set_text('')
    # step_num.set_text('')
    return [line1, line2]

c_len = 0

def animate(i):
    global curve
    global pp_data
    global c_len 
    if len(curve) <= 4:
        return line1, line2, pp_score
    curve = tst.flow_step2(curve, 50)
    if len(curve) != c_len:
        c_len = len(curve)
        print("New length: {}".format(c_len))
    #curve_x, curve_y = np.append(curve[:,0], curve[0,0]), np.append(curve[:,1], curve[0,1])
    curve_x, curve_y = curve[:,0], curve[:,1] #modification propre
    line1.set_data(curve_x, curve_y)
    pp = polsby_popper(curve) #modification
    pp_data = np.append(pp_data, np.array([[i, pp]]), axis=0)
    line2.set_data(pp_data[:,0], pp_data[:,1])
    pp_score.set_text("Step #: {}\nPolsby-Popper score:\n {}".format(i, pp))
    # step_num.set_text("Step #:\n {}".format(i))
    return line1, line2, pp_score

def polsby_popper(closed_curve): 
    region = geom.Polygon(closed_curve)
    return (4 * np.pi * region.area) / (region.length ** 2)

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames= 100, interval=1, blit=True)

Writer = animation.writers['ffmpeg']
ffmpeg = Writer(fps=6, metadata=dict(artist='Me'), bitrate=1000) 
anim.save('Test3.mp4', writer=ffmpeg)
# anim.save('curve_animation.html', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()