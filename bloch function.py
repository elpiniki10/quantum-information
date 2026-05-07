# -*- coding: utf-8 -*-
"""
Block vector ->blochvector()
blochvectorlength-> lenght of bloch vector
bloch_criterion-> criterion of pure or mixed state based on bloch vec length
"""

import qutip as qt
import numpy as np
from qutip import Qobj
from qutip import Bloch

def blochvector(rho:Qobj,x:Qobj,y:Qobj,z:Qobj):
    rx = (rho * x).tr().real
    ry = (rho * y).tr().real
    rz = (rho * z).tr().real
    r = np.array([rx, ry, rz])
    return r
def blochvectorlength(r):
    length= np.linalg.norm(r)
    return length

def bloch_criterion (length:float):
    if np.isclose(length, 1):
        x= "pure state"
    elif np.isclose(length, 0):
        x="maximally mixed state"
    else:
        x="mixed state" 
    return x
def bloch_sphere(r):
    b=Bloch()
    b.add_vectors(r)
    b.show()
#test
psi = (qt.basis(2,0) + qt.basis(2,1)).unit()
rho = qt.ket2dm(psi)
sx = qt.sigmax()
sy = qt.sigmay()
sz = qt.sigmaz()
r=blochvector(rho,sx,sy,sz)
print(r)
l=blochvectorlength(r)
print(l)
print(bloch_criterion (l))
bloch_sphere(r)