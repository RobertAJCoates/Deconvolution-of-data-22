import numpy as np, matplotlib.pyplot as plt, scipy as sc
from testfn import xstepfn,ystepfn
from kernal import t,u1
from convolution import continuousFourierconvol, discreteFourierconvol
stepfn = (xstepfn,ystepfn)
print(xstepfn.size,ystepfn.size,t,u1)
#convolutestepfn
convol_stepfn = continuousFourierconvol(ystepfn,u1)#--->contFourier used cos g1(t) is a cont. fn
#add guass noise
#convol_stepfn_plusnoise = ()
#plot graphs
figs,axs =plt.subplots(2,2)
axs[0,0].step(xstepfn,ystepfn)
axs[0,0].plot(t,u1)
axs[0,1].plot(convol_stepfn)
#axs[1,1].plot(convol_stepfn_plusnoise)
plt.savefig("stepfnbconvol.png")
plt.show()