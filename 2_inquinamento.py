'''
INQUINANTI ATMOSFERICI COPERNICUS
Dati che mostra andamento di inquinanti nel tempo a Perugia.
'''

#Leggi file e fai grafico di andamento (NB scala di tempi convenienti)
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
from scipy import constants, fft
from scipy import optimize

tab=pd.read_csv('copernicus_PG_selected.csv')
time=tab['date']
co=tab['mean_co_ug/m3']
pm10=tab['mean_pm10_ug/m3']
pm2=tab['mean_pm2p5_ug/m3']
so2=tab['mean_so2_ug/m3']
nh3=tab['mean_nh3_ug/m3']
no2=tab['mean_no2_ug/m3']
o3=tab['mean_o3_ug/m3']

plt.figure(figsize=(12,8))
plt.plot(time, co, label='CO')
plt.plot(time, pm10, label='PM10')
plt.plot(time, pm2, label='PM2P5')
plt.plot(time, so2, label='SO2')
plt.plot(time, nh3, label='NH3')
plt.plot(time, no2, label='NO2')
plt.plot(time, o3, label='O3')
plt.legend()
plt.xlabel('Tempo giuliano')
plt.ylabel('Concentrazione ug/m3')
plt.title("Concentrazioni di sostenze nell'atmosfera")
plt.show()

#Monitora CO: fai trasformata, fai grafico spettro di potenza per frequenza e individua andamento
fr_co=fft.fft(co.values)
dt=time[1]-time[0]
freq_co=0.5*fft.fftfreq(len(co), d=dt)
mod2_co=abs(fr_co[1:len(co)//2])**2

plt.figure(figsize=(11,5))
plt.plot(freq_co[1:len(co)//2], mod2_co, color='teal')
plt.title('Spettro di potenza')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Frequenze')
plt.ylabel('|c_k|^2')
plt.legend()
plt.show()

def fit(x, k, beta):
    return k*pow((1/x), beta)

par_co, pcov_co = optimize.curve_fit(fit, xdata=freq_co[50:len(co)//2], ydata=mod2_co[49:], p0=[3, 1], absolute_sigma=True)
print('DATA CO _ Parametri estratti dal fit: ', par_co)
fit_co=fit(freq_co[1:len(co)//2], par_co[0], par_co[1])

plt.figure(figsize=(11,5))
plt.plot(freq_co[1:len(co)//2], mod2_co, color='teal', label='Data CO')
plt.plot(freq_co[1:len(co)//2], fit_co, color='red', label='Fit_CO')
plt.title('Spettro di potenza e fit')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Frequenze')
plt.ylabel('|c_k|^2')
plt.show()

#Spettro di potenza nel periodo e ragiona
plt.figure(figsize=(11,5))
plt.plot(1/freq_co[1:len(co)//2], mod2_co, color='teal')
plt.title('Spettro di potenza')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Periodo')
plt.ylabel('|c_k|^2')
plt.show()

#Fai maschera per estrarre andamento di lungo periodo only
fftmask_co = abs(fr_co)**2 < 1e8
filter_co = fr_co.copy()
filter_co[fftmask_co]=0
# Trasformata FFT inversa con coefficienti filtrati 
co_filter = fft.irfft(filter_co, n=len(co))

plt.figure(figsize=(12,8))
plt.plot(time, co, label='CO')
plt.plot(time, co_filter, label='CO filtered')
plt.legend()
plt.xlabel('Tempo giuliano')
plt.ylabel('Concentrazione ug/m3')
plt.title("Concentrazione di CO nell'atmosfera")
plt.show()





#Fai per un altro inquinante
fr_co=fft.fft(co.values)
dt=time[1]-time[0]
freq_co=0.5*fft.fftfreq(len(co), d=dt)
mod2_co=abs(fr_co[1:len(co)//2])**2

plt.figure(figsize=(11,5))
plt.plot(freq_co[1:len(co)//2], mod2_co, color='teal')
plt.title('Spettro di potenza')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Frequenze')
plt.ylabel('|c_k|^2')
plt.legend()
plt.show()

def fit(x, k, beta):
    return k*pow((1/x), beta)

par_co, pcov_co = optimize.curve_fit(fit, xdata=freq_co[50:len(co)//2], ydata=mod2_co[49:], p0=[3, 1], absolute_sigma=True)
print('DATA CO _ Parametri estratti dal fit: ', par_co)
fit_co=fit(freq_co[1:len(co)//2], par_co[0], par_co[1])

plt.figure(figsize=(11,5))
plt.plot(freq_co[1:len(co)//2], mod2_co, color='teal', label='Data CO')
plt.plot(freq_co[1:len(co)//2], fit_co, color='red', label='Fit_CO')
plt.title('Spettro di potenza e fit')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Frequenze')
plt.ylabel('|c_k|^2')
plt.show()

#Spettro di potenza nel periodo e ragiona
plt.figure(figsize=(11,5))
plt.plot(1/freq_co[1:len(co)//2], mod2_co, color='teal')
plt.title('Spettro di potenza')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Periodo')
plt.ylabel('|c_k|^2')
plt.show()

#Fai maschera per estrarre andamento di lungo periodo only
fftmask_co = abs(fr_co)**2 < 1e8
filter_co = fr_co.copy()
filter_co[fftmask_co]=0
# Trasformata FFT inversa con coefficienti filtrati 
co_filter = fft.irfft(filter_co, n=len(co))

plt.figure(figsize=(12,8))
plt.plot(time, co, label='CO')
plt.plot(time, co_filter, label='CO filtered')
plt.legend()
plt.xlabel('Tempo giuliano')
plt.ylabel('Concentrazione ug/m3')
plt.title("Concentrazione di CO nell'atmosfera")
plt.show()
