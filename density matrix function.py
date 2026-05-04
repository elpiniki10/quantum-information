# -*- coding: utf-8 -*-
"""
density matrix of a pure state
"""
import qutip as qt
from qutip import Qobj

def density_matrix(psi:Qobj)-> Qobj:
    bra = psi.dag()
    rho = psi * bra
    return rho
#tests       
psi1 = qt.rand_ket(7)
print(density_matrix(psi1))