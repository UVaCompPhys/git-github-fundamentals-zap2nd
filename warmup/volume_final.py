from math import pi
from scipy.special import gamma
import numpy as np
from matplotlib import pyplot as plt

def vol_func(n, rad): 
    return (pi**(n/2))*(rad**n)/(gamma(n/2 + 1))

n_arr = np.arange(27, 51, 1)
rad_arr = np.arange(1, 2.05, 0.05)

for n in n_arr:
    string_n = str(n)
    plt.plot(rad_arr, vol_func(n, rad_arr), label=f"n = %s" % string_n)

plt.legend()
plt.xlabel('R = [1, 2]', fontsize = 20)
plt.ylabel('Volume', fontsize = 20)
plt.show()