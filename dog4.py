# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 21:29:50 2021

@author: zeng_
"""

from fabrik import FabrikSolver

import numpy as np
import math

points=np.zeros((3,2),float)

points[1]=[30,-107]
angle=-30/180*math.pi
lens=138.5
points[2]=points[1]+[math.cos(angle)*lens,math.sin(angle)*lens]

print(points)

diff=np.array([5,0])
diff1=np.array([-15,20])

fab=FabrikSolver(points,0.01)
fab1=FabrikSolver(points,0.01)
fab2=FabrikSolver(points,0.01)
fab3=FabrikSolver(points,0.01)


angle0=np.copy(fab.CalAngle())
print('init angle=',angle0)

deviate=fab.ComputeDiff(diff1)
fab1.ComputeDiff(diff)
fab2.ComputeDiff(diff)
fab3.ComputeDiff(diff)

angle1=np.copy(fab.CalAngle())
print('result angle=',angle1)

angle1=(angle1-angle0)
print(angle1)
angle1[1]-=angle1[0]
print(angle1)

angle2=np.copy(fab2.CalAngle())
print('result angle2=',angle2)

angle2=(angle2-angle0)
print(angle2)
angle2[1]-=angle2[0]
print(angle2)

#print(fab.points)
#print(fab1.points)