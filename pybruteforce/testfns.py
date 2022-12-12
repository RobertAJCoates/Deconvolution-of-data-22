import numpy as np, matplotlib.pyplot as plt
#test fn 1: unit stepfn
def step(x):
    return np.heaviside(x+0.5, 0) - np.heaviside(x-0.5,0) 
n1=8
xstepfn = np.arange(-2, 2,1/n1)
ystepfn = step(xstepfn)
#test fn 2: 3x3 matrix with randomly generated values between 0 --> 9
def randvals():
    a = np.zeros(3)
    for i in range(0,3):
        a[i] =np.random.randint(0,10)
    return a