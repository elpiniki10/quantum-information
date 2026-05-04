# -*- coding: utf-8 -*-
"""
Creates a random quantum d-dimensional state

 

    :param dims: int representing dimensions of quantum state

    :return: Qobj representing d-dimensional state

"""
import qutip as qt
from qutip import Qobj
def random_state(dims: int) -> Qobj:
    
    if type(dims) != int:

        raise ValueError('Dimensions should be an integer value')

    psi = qt.rand_ket(dims)

    return psi


psi = random_state(dims=2)

print(psi)
