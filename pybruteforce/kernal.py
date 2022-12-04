import numpy as np, matplotlib.pyplot as plt
#Test 1 g(t) = sin(t)
from testfn import n1
freq = np.pi/n1
def g1(t):
    return np.sin(t) 
t = np.arange(0, n1*np.pi, freq)
u1 = np.sin(t)
print(u1.size, t.size)
