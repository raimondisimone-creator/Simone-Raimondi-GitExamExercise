import numpy as np
import matplotlib.pyplot as plt
import math
import scipy as sp

def HelloWorld():
    print("Hello World!")

def PlotSineWave():
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)
    plt.plot(x, y)
    plt.title("Sine Wave")
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    plt.grid()
    plt.show()

def CalculateFactorial(n):
    if n < 0:
        raise ValueError("Il Fattoriale non è definito per numeri negativi.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * CalculateFactorial(n - 1)
    
def SolveQuadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "Le radici sono complesse."
    elif discriminant == 0:
        root = -b / (2*a)
        return f"La radice è unica: {root}"
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"Le radici sono: {root1} e {root2}"