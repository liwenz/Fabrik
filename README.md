Fabrik inverse kinematics.
A very small and flexible implementation of the Fabrik algorithm. Useful for animation, robotics or other optimization problems. This module is written in python.

fabrik.py : 
fabrik class,it resolve unconstrained ik single chain.It could be 2D,3D or nD
init: input ik init position and marginOfError.
distance: calculate distance between two points
Compute: input new end point and get fabrik result.
ComputeDiff: input new end point's difference and get fabrik result.
calAngle: get current angles.
isReachable: check the result is possible.

test.py:
It's a demo.
construct points array with two way, then fabrik ,print the result

dog.py
dog's one leg's calculate demo
get the result angles array

dog4.py
dog's 4 legs' calculate demo
get the result array
