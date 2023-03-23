import numpy as np
import math

def F(A,x):
    w = len(A)-1
    wynik = 0
    q = 1
    while (w>=0):
        wynik = wynik + q * A[w]
        q = q * x
        w = w-1
    return wynik

def Gorczynski_Piotr_bisekcja(a,b,eps):
    while (abs(a-b)>eps):
        c = (a + b) / 2
        if(abs(F(A,c)) <= eps):
            break
        if(F(A,c) * F(A,a) < 0):
            b=c
        else:
            a=c
    return c

a = -6
b = -2
A = [1,4,3]
eps = 0.1
print(Gorczynski_Piotr_bisekcja(a, b, eps))