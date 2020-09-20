from qutip import *
import scipy 
import numpy
import matplotlib.pyplot as plt
import math
from Rx import *
from Rz import *
from Cz import *

def evenBlock(theta): #input theta is a length 4 list
    U = tensor(Rz(theta[0]), Rz(theta[1]), Rz(theta[2]), Rz(theta[3]))
    C1 = Cz(0,1)
    C2 = Cz(0,2)
    C3 = Cz(0,3)
    C4 = Cz(1,2)
    C5 = Cz(1,3)
    C6 = Cz(2,3)

    Even = C6 * C5 * C4 * C3 * C2 * C1 * U
    
    return Even


def oddBlock(theta): #input theta is a length 4 list
    Odd = tensor(Rx(theta[0]), Rx(theta[1]), Rx(theta[2]), Rx(theta[3]))

    return Odd




def layer(theta, phi): #inputs theta and phi are length 4 lists. first angle is argument for oddBlock
    T = evenBlock(phi) * oddBlock(theta)

    return T
    
    
def preparedVector(L,Theta): #Theta is length 8L. First 4L are even angles, last 4L are odd angles L is number of layers
    xi = tensor(basis(2,0), basis(2,0), basis(2,0), basis(2,0))
    theta = Theta[0:4*L]
    phi = Theta[4*L:8*L]

    for j in range(0,4*L,4):
        xi = oddBlock([phi[j], phi[j+1], phi[j+2], phi[j+3]])*xi
        xi = evenBlock([theta[j],theta[j+1],theta[j+2],theta[j+3]])*xi

    return xi 
        
    

def objFunction(Theta,L,psi): #objective function for finding the minimum distance to the vector psi
     x = preparedVector(L,Theta) - psi
     ep = x.norm()

     return ep


def distanceMinimizer(psi, L): #psi is the random vector, L is the max depth
    d = []
    for j in range(1,L+1):
        y = scipy.optimize.minimize(objFunction, numpy.zeros(8*j), args=(j,psi),method = None, jac=None, hess=None, hessp=None, bounds = None, constraints=(), tol=None, callback=None, options=None).fun
        d.append(y)

    return d
        
        
    






    
