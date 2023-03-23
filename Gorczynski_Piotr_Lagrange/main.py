import numpy as np
import matplotlib.pyplot as plt

def Gorczynski_Piotr_lagrange(x, xw, yw, n):
    q = [0] * len(x)
    for k in range(len(x)):
        for i in range(n+1):
            iloczyn = 1
            for j in range(n+1):
                if(i!=j):
                    iloczyn = iloczyn * ((x[k]-xw[j])/(xw[i]-xw[j]))
            q[k] = q[k] + iloczyn * yw[i]
    return q

x = [1,3,6]
xw = [-2, 1, 4]
yw = [5, 3, 7]
n = 2
print(Gorczynski_Piotr_lagrange(x, xw, yw, n))



def Gorczynski_Piotr_Efekt_Runge(k):
    for i in range(1, k+1):
        plt.subplot(1, 2, 1)
        n = 2*i
        xw = np.linspace(-1, 1, n+1)
        yw = abs(xw)
        x = np.linspace(-1, 1, 150)
        f1 = Gorczynski_Piotr_lagrange(x, xw, yw, n)
        f2 = abs(x)

        plt.xlabel("Oś x")
        plt.ylabel("Oś y")

        plt.title("Wizualizacja efektu Rungego", fontsize = 9)
        plt.plot(x, f2, color = "purple", linewidth = 2)
        plt.plot(x, f1)


        plt.subplot(1,2,2)

        roznica = f1 - f2

        plt.title("Analiza bledu interpolacji", fontsize=9)
        plt.xlabel("Oś x")
        plt.plot(x, roznica)

    plt.show()

Gorczynski_Piotr_Efekt_Runge(6)
