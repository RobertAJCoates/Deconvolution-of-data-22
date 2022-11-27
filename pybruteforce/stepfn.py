import numpy as np, matplotlib.pyplot as plt
#test fn: step fn; create fn using np arrays
n=16
x = np.arange(0,n,1)
y =np.zeros(n)
for i in np.arange(3,13,1):
    y[i] = 2
#calculate convolution of step fn (F is fourier) 
t_fftfreq = np.fft.fftfreq(n,d = 1x.size)
x_fft = np.fft.fft(x)
t_fft = x_fft * t_fftfreq#--->g(t)
y_fft = np.fft.fft(y)#--->f(x)
ytfft = y_fft * t_fft #---> F(f*g) = Ff * Fg ---->convolution 
Fyt = np.fft.ifftshift(np.round(np.real(ytfft)))#--->ifftshift [inverse fftshift]: shifts zero freq component 2 centre of spectrum
#add guassian noise

#plot graphs (stepfn, convoluted stepfn, convoluted stepfn with gaussain)
figs,axs = plt.subplots(1,2)
axs[1].step(x,y)
axs[0,1].plot(Fyt)
plt.savefig('stepfntest.png')
plt.show()