''' COLORI DEI RUMORI
Ci sono diversi tipi di rumore, presenti in dati reali, legati a fenomeni stocastici. Possono essere intrinsechi o relativi alm etodo di acquisizione dati.
L'andamnento del power spectrum associa un colore al rumore.
-bianco: tutte frequenze hanno tessa oscillazione, andamento costante;
-rosa: andamento 1/f;
-rosso (o brown per moto browniano): va come 1/f^2;
In generale, 1/f^\beta (source: wikipedia).
'''


import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
from scipy import constants, fft
from scipy import optimize

#Leggi i tre file e fai grafico segnali
tab1=pd.read_csv('data_sample1.csv')
tab2=pd.read_csv('data_sample2.csv')
tab3=pd.read_csv('data_sample3.csv')
print(tab1)
print(tab2)
print(tab3)

t1=tab1['time']
a1=tab1['meas']
t2=tab2['time']
a2=tab2['meas']
t3=tab3['time']
a3=tab3['meas']

plt.figure(figsize=(12,5))
plt.plot(t1, a1, color='salmon', label='Data1')
plt.plot(t2, a2, color='mediumspringgreen', label='Data2')
plt.plot(t3, a3, color='cornflowerblue', label='Data3')
plt.xlabel('Time')
plt.ylabel('Amplitude [UA]')
plt.title('Dati misurati')
plt.legend()
plt.show()

#Fai trasformata di fourier di tre segnali ed estrai spettro di potenza
fr1=fft.fft(a1.values)
dt1=t1[1]-t1[0]
freq1=0.5*fft.fftfreq(len(a1), d=dt1)
p1=abs(fr1[5:len(a1)//2])**2
fr2=fft.fft(a2.values)
dt2=t2[1]-t2[0]
freq2=0.5*fft.fftfreq(len(a2), d=dt2)
p2=abs(fr2[5:len(a2)//2])**2
fr3=fft.fft(a3.values)
dt3=t3[1]-t3[0]
freq3=0.5*fft.fftfreq(len(a3), d=dt3)
p3=abs(fr3[5:len(a3)//2])**2

plt.figure(figsize=(11,5))
plt.plot(freq1[5:len(a1)//2], p1, color='salmon', label='Data1', alpha=0.6)
plt.plot(freq2[5:len(a2)//2], p2, color='mediumspringgreen', label='Data2', alpha=0.6)
plt.plot(freq3[5:len(a3)//2], p3, color='cornflowerblue', label='Data3', alpha=0.6)
plt.title('Spettri di potenza')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Frequenze')
plt.ylabel('|c_k|^2')
plt.legend()
plt.show()

#Fai fit di spettro di potenza per capire di quale colore siano
def fit(x, k, beta):
    return k*pow((1/x), beta)

par1, pcov1 = optimize.curve_fit(fit, xdata=freq1[5:len(a1)//2], ydata=p1, p0=[3, 1], absolute_sigma=True)
print('DATA1 _ Parametri estratti dal fit: ', par1)
fit1=fit(freq1[5:len(a1)//2], par1[0], par1[1])
par2, pcov2 = optimize.curve_fit(fit, xdata=freq2[5:len(a2)//2], ydata=p2, p0=[3, 1], absolute_sigma=True)
print('DATA2 _ Parametri estratti dal fit: ', par2)
fit2=fit(freq2[5:len(a2)//2], par2[0], par2[1])
par3, pcov3 = optimize.curve_fit(fit, xdata=freq3[5:len(a1)//2], ydata=p3, p0=[3, 2], absolute_sigma=True)
print('DATA3 _ Parametri estratti dal fit: ', par3)
fit3=fit(freq3[5:len(a3)//2], par3[0], par3[1])

plt.figure(figsize=(11,5))
plt.plot(freq1[5:len(a1)//2], p1, color='salmon', label='Data1', alpha=0.6)
plt.plot(freq1[5:len(a1)//2], fit1, color='red', label='Fit1')
plt.plot(freq2[5:len(a2)//2], p2, color='mediumspringgreen', label='Data2')
plt.plot(freq2[5:len(a2)//2], fit2, color='forestgreen', label='Fit2')
plt.plot(freq3[5:len(a3)//2], p3, color='cornflowerblue', label='Data3')
plt.plot(freq3[5:len(a3)//2], fit3, color='blue', label='Fit3')
plt.title('Spettri di potenza e fit')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Frequenze')
plt.ylabel('|c_k|^2')
plt.legend()
plt.show()
