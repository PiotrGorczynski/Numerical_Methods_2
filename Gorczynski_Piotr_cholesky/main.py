import numpy as np
from math import sqrt

def Gorczynski_Piotr_rozklad_cholesky(A):
    L = len(A)
    wynik = np.zeros_like(A)

    for k in range(L):
        wynik[k, k] = sqrt(A[k, k])
        wynik[k, k + 1:] = A[k, k + 1:]/wynik[k, k]
        for j in range(k + 1, L):
            A[j, j:] = A[j, j:] - wynik[k, j] * wynik[k, j:]

    return wynik


A = np.array([[4, -6, 8],[-6, 10, -10],[8, -10, 29]])
print(Gorczynski_Piotr_rozklad_cholesky(A))