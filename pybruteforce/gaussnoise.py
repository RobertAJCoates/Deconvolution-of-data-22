import numpy as np, matplotlib.pyplot as plt
from scipy.stats import norm
mean, var, skew, kurt = norm.stats(moments='mvsk')
xgnoise = np.linspace(norm.pdf(0.00),norm.pdf(0.99),32)
randvars = np.random.normal(0,1, size = 32)
freezerv = norm()
ygnoise= freezerv.pdf(xgnoise)
ygnoiserand = ()
plt.plot(xgnoise,ygnoise)
plt.show()