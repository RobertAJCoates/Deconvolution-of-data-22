import numpy as np, matplotlib.pyplot as plt, scipy as sc
from testfns import xstepfn,ystepfn
from kernalfns import t,u1
from convolution import continuousFourierconvol
from gaussnoise import xgnoise,ygnoiserand
#convolutestepfn
convol_stepfn = continuousFourierconvol(ystepfn,u1)#--->contFourier used cos g1(t) is a cont. fn
#add guass noise
noisestepfn = ygnoiserand
convol_stepfn_plusnoise = convol_stepfn + noisestepfn
print(convol_stepfn_plusnoise)
#plot graphs
figs,axs =plt.subplots(2,2)
axs[0,0].step(xstepfn,ystepfn)
axs[0,0].plot(t,u1)
axs[0,1].plot(xstepfn,convol_stepfn)
axs[1,0].plot(xgnoise,noisestepfn)
axs[1,1].plot(xgnoise,convol_stepfn_plusnoise)
plt.savefig("stepfnbconvol.png")
plt.show()