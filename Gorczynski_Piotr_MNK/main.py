import numpy as np
import math
import copy

#funkcje z poprzedniej pd nie wspolgraly idk - wyskakiwaly lekko inne wyniki


def Gorczynski_Piotr_ukladU(L, b):
    wynik = [0] * len(b)
    suma = 0
    w = len(L)
    i = w - 1
    while (i >= 0):
        if (L[i][i] == 0):
            print("Nie dziel przez 0")
            return 0

        for j in range(i + 1, w):
            suma = suma + (L[i][j] * wynik[j])

        wynik[i] = (b[i] - suma) / L[i][i]
        suma = 0
        i = i - 1

    return wynik


def Gorczynski_Piotr_ukladL(L, b):
    wynik = [0] * len(b)
    suma = 0
    w = len(L)
    for i in range(w):
        if (L[i][i] == 0):
            print("Nie dziel przez 0")
            return 0
        for j in range(i):
            suma = suma + (L[i][j] * wynik[j])
        wynik[i] = (b[i] - suma) / L[i][i]
        suma = 0

    return wynik


# run math nie dziala idk why sqrt wykrywa ujemne wartosci
# def Gorczynski_Piotr_rozklad_cholesky(A):
#    L = len(A)
#    wynik = np.zeros_like(A)
#    for k in range(L):
#        wynik[k, k] = sqrt(A[k, k])
#        wynik[k, k + 1:] = A[k, k + 1:] / wynik[k, k]
#        for j in range(k + 1, L):
#            A[j, j:] = A[j, j:] - wynik[k, j] * wynik[k, j:]
#    return wynik


def Gorczynski_Piotr_rozklad_cholesky(A):
    L = [[0] * len(A) for i in range(len(A))]
    for i in range(len(A)):
        for j in range(i + 1):
            if (i == j):
                suma = 0
                for k in range(j):
                    suma = suma + (L[i][k] * L[i][k])
                L[i][i] = math.sqrt(A[i][i] - suma)
            else:
                suma = 0
                for k in range(j):
                    suma = suma + (L[j][k] * L[i][k])
                L[i][j] = (A[i][j] - suma) / L[j][j]
    return L


def Gorczynski_Piotr_MNK(x, y, n):
    a = [1] * len(x)
    A = [[1] * len(x) for i in range(len(x))]
    At = [[1] * len(x) for i in range(len(x))]
    for i in range(len(x)):
        for j in range(1, len(x)):
            A[i][j] = x[i] * A[i][j - 1]

    for i in range(len(x)):
        for j in range(0, len(x)):
            At[i][j] = A[j][i]

    A = np.array(A)
    At = np.array(At)
    y = np.array(y)
    L = At.dot(A)
    p = At.dot(y)
    L = Gorczynski_Piotr_rozklad_cholesky(L)
    U = copy.deepcopy(L)

    for i in range(len(A)):
        for j in range(len(A)):
            U[i][j] = L[j][i]
    z = Gorczynski_Piotr_ukladL(L, p)
    wynik = Gorczynski_Piotr_ukladU(U, z)

    return wynik


x = [1, 3, 4]
y = [1, 2, 4]
print(Gorczynski_Piotr_MNK(x, y, 3))
