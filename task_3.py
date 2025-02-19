import matplotlib.pyplot as plt
import numpy as np

a = 0.1382
b = 3.19 * (10 ** (-5))
R = 8.314
v = np.arange(b + 10 ** (-5), 10 ** (-3), 10 ** (-7))  # объем

def fv(v):
    t = 273.15 - 130
    return R * t / (v - b) - a / v ** 2

def line(maxi, mini):
    eps=10**(-7)
    line=0
    for i in np.arange(mini, maxi, eps):
        a=fv(i)
        b =fv(i+eps)
        del_len = (eps**2 + abs(a-b)**2)**0.5
        line+=del_len
    return line
ma=0.00013611
mi=0.00007195
print(line(ma, mi))