from fabrik import FabrikSolver

import numpy as np
import math

points = np.array([[0,0],[100,0],[100,70]],float)
diff=np.array([-40,20])

#fab=FabrikSolver(points,0.001)
#deviate=fab.ComputeDiff(diff)
#print("deviate=",deviate)
#print(fab.points)

points1=np.zeros((3,2),float)
print(points1)
points1[1]=[30,-107]
angle=-30/180*math.pi
lens=138.5
points1[2]=points1[1]+[math.cos(angle)*lens,math.sin(angle)*lens]


print(points1)



fab=FabrikSolver(points1,0.01)
print(fab.length)
angle0=fab.CalAngle()
print('init angle=',angle0)
deviate=fab.ComputeDiff(diff)

angle1=fab.CalAngle()
print('result angle=',angle1)


print("deviate=",deviate)
print(fab.points)

