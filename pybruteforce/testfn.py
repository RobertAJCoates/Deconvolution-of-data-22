#test fn 1: unit step.fn
import numpy as np, matplotlib.pyplot as plt
def step(x):
    return np.heaviside(x+0.5, 0) - np.heaviside(x-0.5,0) 
n1=8
xstepfn = np.arange(-2, 2,1/n1)
ystepfn = step(xstepfn)