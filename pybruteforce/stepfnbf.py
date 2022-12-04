import numpy as np, matplotlib.pyplot as plt, scipy as sc
from testfn import xstepfn,ystepfn
from kernal import t,u1
from convolution import continuousFourierconvol
stepfn = [xstepfn,ystepfn]
print(stepfn)
print(xstepfn.size,ystepfn.size)
#convolutestepfn
convol_stepfn = continuousFourierconvol(ystepfn,u1)
print(convol_stepfn)
