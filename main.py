import matplotlib.pyplot as plt
import numpy as np

# Задача 1
a = 0.1382
b = 3.19 * (10 ** (-5))
R = 8.314


def VDV_p(v, t):
    t += 273.15
    return R * t / (v - b) - a / v ** 2


f = VDV_p
v = np.arange(b + 10 ** (-5), 10 ** (-3), 10 ** (-7))  # объем


def task_1(T):
    plt.plot(v, f(v, T))
    '''for T in range(-140, -99, 10):   
        plt.plot(v, f(v, T))'''

    plt.axhline(color='black')
    plt.axvline(color='black')
    plt.grid(True)
    plt.show()
    return


# Задача 2

#task_1(-130)
def fv(v):
    t = 273.15 - 130
    return R * t / (v - b) - a / v ** 2

def local(left, right):
    mid_l = left + (right - left) / 3
    mid_r = left + (right - left) * 2 / 3
    if mid_r-mid_l<=10**(-7):
        return mid_l
    mono_2 =(fv(mid_r)-fv(mid_l))/abs(fv(mid_r)-fv(mid_l))
    mono_3 = (fv(right)-fv(mid_r))/abs(fv(right)-fv(mid_r))
    if mono_3==mono_2:
        right=mid_r
    else:
        left=mid_l
    return local(left, right)

maxi=local(0.0001, 0.00016)
mini=local(0, 0.0001)
# print(f'Максимум: {maxi},   Минимум: {mini}')


# Задача 3

def line(maxi, mini):
    eps=10**(-7)
    line=0
    for i in np.arange(mini, maxi, eps):
        a=f(i)
        b = f(i+eps)
        del_len = (eps**2 + abs(a-b)**2)**0.5
        line+=del_len
    return line
# print(line(maxi, mini))


# Задача 4
def fun(v):
    p_0 = 3664186.998
    return fv(v)-p_0
def search_solution(left, right, eps):
    while abs(left-right)>eps:
        mid=(left+right)/2
        if fun(mid)*fun(left)<=0:
            right=mid
        else:
            left=mid
    return left
eps=10**(-7)

plt.plot(v, fun(v))
plt.axhline(color='black')
plt.axvline(color='black')
plt.grid(True)
plt.show()

# print(search_solution(left, right, eps))