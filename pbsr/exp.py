import numpy as np
from scipy.linalg import eigh
import math

def bar(num_elements):

    restrained_dofs = [0,]

    m = np.array([[2, 1], [1, 2]]) / (6. * num_elements)
    k = np.array([[1, -1], [-1, 1]]) * float(num_elements)


    M = np.zeros((num_elements + 1, num_elements + 1))
    K = np.zeros((num_elements + 1, num_elements + 1))
    
    for i in range(num_elements):
        M[i:i+2, i:i+2] += m
        K[i:i+2, i:i+2] += k

    for dof in restrained_dofs:
        M = np.delete(M, dof, axis=0)
        M = np.delete(M, dof, axis=1)
        K = np.delete(K, dof, axis=0)
        K = np.delete(K, dof, axis=1)

    evals, evecs = eigh(K, M)

    frequencies = np.sqrt(evals)

    return frequencies

