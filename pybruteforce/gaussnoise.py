import numpy as np, matplotlib.pyplot as plt
from testfns import xstepfn
print(xstepfn.shape)
def gaussnoisestepfn(mu,stdov,xdash):
    std = stdov*np.std()#-->returns std deviation with stnadard 
    noise = np.random.noise(mu,std,size = xstepfn.shape)
    xnoise = xdash + noise
    return xnoise