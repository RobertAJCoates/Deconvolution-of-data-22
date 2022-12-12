import numpy as np, scipy as sc
#define covolution step for any test function y = f(x) and kernal function u= g(t)
def discreteFourierconvol(y,u):
    return np.fft.fft(y)*np.fft.fft(u)
def continuousFourierconvol(y,u):
    return sc.signal.convolve(y,u, mode = "same")