def F(A,x):
    w = len(A)-1
    wynik = 0
    q = 1
    while (w>=0):
        wynik = wynik + q * A[w]
        q = q * x
        w = w-1
    return wynik

def Gorczynski_Piotr_sieczne(x1, x2, eps):
    xk = x1
    xk_1 = x2
    while (abs(xk_1 - xk)>eps):
        tmp = xk_1 - (((xk_1 - xk) * F(A, xk_1))/(F(A, xk_1) - F(A, xk)))
        xk = xk_1
        xk_1 = tmp
    return xk_1


x1 = -2
x2 = 2
A=[1,0,-1,1]
eps = 0.00000001
print(Gorczynski_Piotr_sieczne(x1, x2, eps))