from qutip import *
import math

#This code defines a CZ gate between sites x,y of the 4 qubit array {0,1,2,3}.
#x is the control and y is the site which is acted on by sigma z.

def Cz(x,y):
    P1 = Qobj([ [0,0], [0,1]])
    P0 = Qobj([ [1,0], [0,0]])
#Pn is the projection onto the nth basis vector, n=0,1
    if x==y:
        print('Sites should differ')
    elif min(x,y)<0:
        print('Sites must be in 0,1,2,3')
    elif max(x,y)>3:
        print('Sites must be in 0,1,2,3')
    else:
        T = Qobj([ [0,0], [0,0]])
        S = Qobj([ [0,0], [0,0]])
# T is, up to non-identity tensor factors, P1 \otimes sigma z
# S is, up to non-identity tensor factors, P0 \otimes identity
# Then CZ = T + S. 
        for a in [0,1,2,3]:
            if a == 0:
                if a == x:
                    T = P1
                    S = P0
                elif a == y:
                    T = sigmaz()
                    S = identity(2)
                else: 
                    T = identity(2)
                    S = identity(2)
            else:                        
                if a == x:
                    T = tensor(T, P1)
                    S = tensor(S, P0)   
                elif a == y:
                    T = tensor(T, sigmaz())
                    S = tensor(S, identity(2))
                else:
                    T = tensor(T, identity(2))
                    S = tensor(S, identity(2))
    return T + S
                
        
