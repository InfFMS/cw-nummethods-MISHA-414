import matplotlib.pyplot as plt
import numpy as np

a = 0.1382
b = 3.19 * (10 ** (-5))
R = 8.314
v = np.arange(b + 10 ** (-5), 10 ** (-3), 10 ** (-7))  # объем

# Задача 2


def fv(v):
    t = 273.15 - 130
    return R * t / (v - b) - a / v ** 2

def local_min(left, right):
    mid_l = left + (right - left) / 3
    mid_r = left + (right - left) * 2 / 3
    if mid_r-mid_l<=10**(-7):
        return mid_l

    if fv(mid_l)<fv(mid_r):
        right=mid_r
    else:
        left=mid_l
    return local_min(left, right)

def local_max(left, right):
    mid_l = left + (right - left) / 3
    mid_r = left + (right - left) * 2 / 3
    if mid_r-mid_l<=10**(-7):
        return mid_l

    if fv(mid_l)>fv(mid_r):
        right=mid_r
    else:
        left=mid_l
    return local_max(left, right)


maxi=local_max(0.0001, 0.00016)
mini=local_min(0, 0.0001)
print(f'Максимум: {maxi},   Минимум: {mini}')