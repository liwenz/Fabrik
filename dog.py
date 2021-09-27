# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 15:52:29 2021

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

fab=FabrikSolver(points,0.01)
print('lenth= ',fab.length)

angle0=np.copy(fab.CalAngle())
print('init angle=',angle0)

deviate=fab.ComputeDiff(diff)

angle1=fab.CalAngle()
print('result angle=',angle1)

angle=(angle1-angle0)
print(angle)
angle[1]-=angle[0]
print(angle)


print("deviate=",deviate)
print(fab.points)