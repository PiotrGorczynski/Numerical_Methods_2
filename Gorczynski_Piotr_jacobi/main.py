import numpy as np


def Gorczynski_Piotr_jacobi(A,b,eps):
    czyzbiezna = True
    w = len(A)
    for i in range(w):
        suma = 0
        for j in range(w):
            suma = suma + abs(A[i][j])
        suma = suma - abs(A[i][i])
        if (abs(A[i][i]) < suma):
            czyzbiezna = False
    if(czyzbiezna!=True):
      return "Macierz nie spelnia warunku zbieznosci"


    n = len(b)
    x = np.zeros(n)
    x0 = np.ones(n)
    while (np.linalg.norm(x0-x) > eps):
        x0 = x.copy()
        for i in range(n):
            x[i] = b[i]
            for j in range(n):
                if (j!=i):
                    x[i]=x[i]-A[i][j]*x0[j]
            x[i]=x[i]/A[i][i]
    return x

A = np.array([[-5,1,2],
     [1,6,3],
     [2,-1,-4]])

B = np.array([[3,-2,1],
     [1,-3,2],
     [-1,2,4]])

C = np.array([[-2,2,1],
     [1,3,2],
     [1,-2,0]])

b = [13,1,-1]

eps = 0.000001
print(Gorczynski_Piotr_jacobi(A,b,eps))