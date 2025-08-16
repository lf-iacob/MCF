#Import
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import norm
from scipy.optimize import curve_fit
import matplotlib.colors as mcolors
import sys,os
import math as mt
import pandas as pd
import scipy as sp
from scipy import optimize
import matplotlib.pyplot as plt
import scipy.odr as odr
from scipy.stats import chi2
from pandas.core.generic import DataFrameRenderer
import collections
import scipy.special
from numpy.lib import mask_indices

# Definizione funzione gaussiana
def gauss_func(x, A, mu, sigma):
    return A*np.exp(-(x-mu)**2/(2*sigma**2))


# Misure
C_C2=np.array([6,6,6,8,8,9,9,9,9,9,9,9,9,9,10,10,10,10,10,11,11,11,11,11,11,11,11,11,11,11,11,11,12,12,12,12,12,12,12,12,12,12,13,13,13,13,13,13,13,13,13,13,13,13,14,14,14,14,14,14,14,14,14,14,14,15,15,15,15,15,15,15,15,15,15,15,16,16,16,16,16,16,16,16,17,17,17,17,17,18,18,18,18,18,18,19,19,20,20,21])
# Estrazione delle frequenze senza zeri (con counts)
iC_C2=np.unique(C_C2, return_counts=True)
FC_C2=iC_C2[1]


# Istogramma
plt.figure(figsize=(8,6))
plt.title('Fit gaussiano', fontsize=14)
# Grafico frequenze misurate sperimentalmente
n,bins,patches=plt.hist(C_C2, 20, range=(4,24), color='blueviolet', label='Misurazioni sperimentali')
# Fit gaussiana
mask=np.nonzero(n)
bincenters=(bins[:-1] + bins[1:])/2
par, pcov = curve_fit(gauss_func, xdata=bincenters[mask], ydata=n[mask], sigma=np.sqrt(n[mask]), p0=[14, 15, 3], absolute_sigma=True)
plt.plot(bincenters, gauss_func(bincenters, par[0], par[1], par[2]), color='deepskyblue', label='Fit gaussiano')
plt.ylabel('Frequenze', fontsize=12)
plt.xlabel('Bins', fontsize=12)
plt.legend()
plt.show()
#OS: la deviazione standard è par[2]


# Chi2 gaussiano
y_gauss=gauss_func(bincenters,par[0],par[1],par[2])
squared_error=np.power((y_gauss[mask]-FC_C2)/np.sqrt(FC_C2),2)
chi2_C_C2=squared_error.sum()
# Definisco i gradi di libertà
gd=FC_C2.size-4
chi2r_C_C2=chi2_C_C2/gd
p_C_C2=sp.stats.chi2.sf(chi2_C_C2,gd,loc=0,scale=1)
print('Chi2=',chi2_C_C2)
print('Probabilità associata al Chi2',p_C_C2)
