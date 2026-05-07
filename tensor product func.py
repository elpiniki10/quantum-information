# -*- coding: utf-8 -*-
"""
Tensor product of 2 quantum states
"""
from qutip import *
from qutip import Qobj

def tensor_product(x:Qobj,y:Qobj)-> Qobj:
    psi = tensor(x,y)
    return psi
 
#tests   
zero = basis(2,0) 
one = basis(2, 1)

print(tensor_product(zero,one))