# -*- coding: utf-8 -*-
"""
 Measurement of an observable of a density matrix
rho->density matrix,obs->observable,
.eigenstates() -> computes eigenvalues and eigenvectors of a matrix.
eigenvalues go first (numbers),eigenvectors second(Qobj vectors)"""

import qutip as qt
from qutip import Qobj

def measurement_observable(rho:Qobj, obs:Qobj):
    eigvals, eigvecs = obs.eigenstates()
    results = []
    expectation_val = (rho * obs).tr()
    for val, vec in zip(eigvals, eigvecs):
        proj = qt.ket2dm(vec) #projector
        prob = (rho * proj).tr() #born(prob of eigval)
        results.append((val, prob))

    return expectation_val,results
#test
psi = (qt.basis(2,0) + qt.basis(2,1)).unit() #.unit()->normalizes the vector
rho = qt.ket2dm(psi)
sx = qt.sigmax()

print(measurement_observable(rho, sx))