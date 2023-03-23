import numpy as np

def Gorczynski_Piotr_rozklad_LU_dolittle(A):
    wymiar = len(A)
    L = [[0 for x in range(wymiar)] for y in range(wymiar)]
    U = [[0 for x in range(wymiar)] for y in range(wymiar)]

    for i in range(wymiar):
        for j in range(i, wymiar):
            suma = 0
            for k in range(i):
                suma = suma + (L[i][k] * U[k][j])
            U[i][j] = A[i][j] - suma
        for j in range(i, wymiar):
            if (i==j):
                L[i][i] = 1
            else:
                suma = 0
                for k in range(i):
                    suma = suma + (L[j][k] * U[k][i])
                L[j][i] = int((A[j][i] - suma)/U[i][i])

    print('Dolna\t\t\tGórna')

    for i in range(wymiar):
        # dolna
        for j in range(wymiar):
            print(L[i][j], end="\t")
        print("", end="\t")

        # górna
        for j in range(wymiar):
            print(U[i][j], end="\t")
        print("")

    return L, U

A=np.array([[2, 5, 7],[6, 3, 4],[5, -2, -3]])
Gorczynski_Piotr_rozklad_LU_dolittle(A)