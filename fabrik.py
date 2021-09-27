# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 13:26:39 2021

@author: zeng_
"""

import numpy as np
import math

class FabrikSolver:
    """ 
        An inverse kinematics solver in Fabrik Algorithm.
    """
    def __init__(self, _points, _marginOfError=0.01):
        self.points=np.copy(_points)
        self.marginOfError=_marginOfError
        self.ndim=self.points.ndim
        self.number=int(self.points.size/self.ndim)
        self.length=np.zeros(self.number-1,dtype=float)
        self.angle=np.zeros(self.number-1,dtype=float)
        #print('ndim= ',self.ndim)
        #print('number= ',self.number)

        self.maxLenth=0.0
        for i in range(self.number-1):
            self.length[i] = self.distance(self.points[i],self.points[i+1])
            self.maxLenth+=self.length[i]
            #print(self.length[i])
        #print('maxlenth= ',self.maxLenth)
    def distance(self,a,b):
        dist=0.0
        for i in range(self.ndim):
            dist=dist+(a[i]-b[i])*(a[i]-b[i])
        dist=math.sqrt(dist)
        return dist
    def CalAngle(self):
        for i in range(self.number-1):
            p=self.points[i+1]-self.points[i]
            self.angle[i]=math.atan2(p[1], p[0])*180/math.pi
        return self.angle



    def Backword(self):
        #print("backword")
        self.points[self.number-1]=self.target
        for i in range(self.number-1):
            q=self.number-1-i
            l=self.distance(self.points[q], self.points[q-1])
            r=self.length[q-1]/l
            #print(i,q,l,r)
            self.points[q-1]=self.points[q-1]*r+self.points[q]*(1-r)
        #print(self.points)
        
    def Forword(self):
        self.points[0]=np.zeros(self.ndim,dtype=float)
        #print("forword")
        for i in range(self.number-1):
            q=i+1
            l=self.distance(self.points[q], self.points[q-1])
            r=self.length[q-1]/l
            #print(i,q,l,r)
            self.points[q]=self.points[q]*r+self.points[q-1]*(1-r)
        #print(self.points)
    def Compute(self,target):
        self.target=target
        print("target= ",self.target)
        if(not(self.isReachable())):
            print("is Not Reachable")
            return 100
        deviate=10000
        while(deviate>self.marginOfError):
            self.Backword()
            self.Forword()
            deviate=self.distance(self.points[self.number-1],self.target)
            #print('deviate= ',deviate)
        return deviate
    def ComputeDiff(self,targetDiff):
        return self.Compute(targetDiff+self.points[self.number-1])
    
    def isReachable(self):

        return (self.maxLenth>=self.distance(self.points[0],self.target))
    



