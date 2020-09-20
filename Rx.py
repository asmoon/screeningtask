from qutip import *
import math

def Rx(theta):
    x = theta/2
    Rx = Qobj([ [math.cos(x), -complex(0,math.sin(x))], [-complex(0,math.sin(x)), math.cos(x)]] )
    return Rx
    
