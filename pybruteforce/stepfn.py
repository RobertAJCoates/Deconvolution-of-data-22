import numpy as np, matplotlib.pyplot as plt
'''
Test Fn: Stepfn.py
'''
n=16
x = np.arange(0,n,1)
y =np.zeros(n)
for i in np.arange(4,12,1):
    y[i] = 2
#plot stepfn onto graph

figs,axs = plt.subplots(2,2)
axs[0,0].step(x,y)


#calculate convolution of step fn (F is fourier)
x_fft = np.fft.fft(x)#--->F(x)
y_fft = np.fft.fft(y)#--->F(y)
yyfft = y_fft * y_fft #---> F(x * y) = F(x) * F(y)
Fyy = np.fft.ifftshift(np.round(np.real(yyfft)))
print(Fyy)
axs[1,1].plot(yyfft)
axs[1,0].plot(Fyy)
plt.savefig('stepfntest.png')
plt.show()

