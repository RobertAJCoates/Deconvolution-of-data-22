import numpy as np, matplotlib.pyplot as plt
#Test 1 g(t) = sin(t)
from testfns import n1
freq = np.pi/n1
def g1(t):
    return (np.cos(t))**2
a = freq * (n1/2)
b = a + freq
t = np.arange(-a,a,freq)
u1 = g1(t)