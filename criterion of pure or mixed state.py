# -*- coding: utf-8 -*-
"""
criterion of whether a state is pure or mixed
"""
#crit with purity
import numpy as np
import qutip as qt
from qutip import Qobj
def criterion_pure_mixed(rho:Qobj):
    purity = (rho * rho).tr()
    if np.isclose(purity, 1):
        rho= "pure state"
    elif np.isclose(purity, 0):
        rho="maximally mixed state"
    else:
        rho="mixed state"
    return rho
#tests        
zero = qt.basis(2, 0)
rho_pure = qt.ket2dm(zero)
one = qt.basis(2, 1)
rho_mixed = 0.5 * qt.ket2dm(zero) + 0.5 * qt.ket2dm(one)
print(criterion_pure_mixed(rho_pure ))
print(criterion_pure_mixed(rho_mixed ))

#crit with entropy
def vonneumann_entropy(rho:Qobj):
    S = qt.entropy_vn(rho, base=2)
    if np.isclose(S, 0):
       x="pure state"
    elif np.isclose(S, 1.0):
       x="mixed state"
    return x
#tests
print(vonneumann_entropy(rho_mixed))