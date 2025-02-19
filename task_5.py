import matplotlib.pyplot as plt
import numpy as np

a = 0.1382
b = 3.19 * (10 ** (-5))
R = 8.314
v = np.arange(b + 10 ** (-5), 10 ** (-3), 10 ** (-7))  # объем

# Задача 5
def VDV(v):
    t=273.15-130
    return R*t/(v-b) - a/v**2

V_1=6.15* 10**-5
V_g=0.0001947

p_0 = 3664186.998
eps=10**-7


def integral(v, left, right, f, eps):
    fig, ax = plt.subplots()
    ax.plot(v, f(v))

    v0=left
    square=0
    while v0<right:
        average_value=(f(v0)+f(v0+eps))/2
        # Прямоугольник
        rect = plt.Rectangle((v0+eps/2, 0), eps, average_value, color="red")
        ax.add_patch(rect)

        del_area=average_value*eps
        square+=del_area
        v0+=eps
    print(square)
    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.grid(True)
    plt.show()
    return square
t=-130

integral(v, V_1, V_g, VDV, eps)
