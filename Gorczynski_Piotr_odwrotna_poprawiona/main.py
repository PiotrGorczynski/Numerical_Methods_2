import numpy as np


def schodkowa(A):
    for i in range(len(A)):
        w1 = A[i, i]
        for j in range(i, len(A[0])):
            A[i, j] = A[i, j]/w1
        for k in range(i + 1, len(A)):
            w = A[k, i]/A[i, i]
            for l in range(i, len(A[0])):
                A[k, l] = A[k, l] - A[i, l] * w
    return A

def jednostkowa(i, j):
    I = np.zeros([i, j])
    for t in range(j):
        I[t, t] = 1
    return I


def Gorczynski_Piotr_macierz_odwrotna(A):
    I = jednostkowa(len(A), len(A[0]))
    Ap = np.append(A, I, 1)
    Ap = schodkowa(Ap)

    for i in range(len(A[0]) - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            tmp = Ap[j, i]
            for k in range(i, len(Ap[0])):
                Ap[j, k] = Ap[j, k] - Ap[i, k] * tmp

    return Ap[:, len(A[0]):len(Ap[0])]


B = np.array([[2, 5, 7], [6, 3, 4], [5, -2, -3]])

print(Gorczynski_Piotr_macierz_odwrotna(B))

