from qutip import *
import cmath

#This function defines an Rz gate with angle of rotation theta. 

def Rz(theta):
    x = complex(0,theta/2)
    Rz = Qobj([ [cmath.exp(x), 0], [0, cmath.exp(x)]])
    return Rz
    
