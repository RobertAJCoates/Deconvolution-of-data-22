import numpy as np, matplotlib.pyplot as plt
#test fn: step fn; create fn using np arrays
n=100
freq = n/np.pi
#def x and f(x)---->call y
x = np.arange(0,n,1)
y =np.zeros(n)
for i in np.arange(25,75):
    y[i] = 1
#def t and g(t)-->call u
t = np.arange(0,np.pi,1/(freq))
u = (np.sin((t)))**2
print(x.size,t.size)
#calculate convolution of step fn (F is fourier) 
y_fft = np.fft.fft(y)#--->f(x)
u_fft = np.fft.fft(u)#--->g(t)
ytfft = y_fft * u_fft #---> F(f*g) = Ff(x) * Fg(t) ---->convolution
print(ytfft)
Fyt = np.fft.ifftshift(np.round(np.real(ytfft)))#--->ifftshift [inverse fftshift]: shifts zero freq component 2 centre of spectrum
#add guassian noise

#brute force deconvolute - use for, while or if loops to save time but probably not that much time in reality

#plot graphs (stepfn, convoluted stepfn, convoluted stepfn with gaussain)
figs,axs = plt.subplots(2,2)
axs[0,0].step(x,y)
axs[1,0].plot(t,u)
axs[0,1].plot(ytfft)
plt.savefig('stepfntest.png')
plt.show()