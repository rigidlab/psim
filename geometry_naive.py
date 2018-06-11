import sympy 
import numpy 

class Vector:
    def __init__(self,start,end):
        """
        Return a vector object 
        """
        pass

class Point(object):
    def __init__(self,x,y,z,frame,name=None):
        """
        x,y,z: x,y,z Cartesian coordinate of the point 
        Return a point object
        """
        self.x,self.y,self.z = x,y,z
        self.frame = frame 

    def __repr__(self):
        return "Point ({},{},{})".format(self.x,self.y,self.z)

        
