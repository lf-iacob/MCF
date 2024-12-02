'''
INQUINANTI ATMOSFERICI COPERNICUS
Dati che mostra andamento di inquinanti nel tempo a Perugia.
'''

#Leggi file e fai grafico di andamento (NB scala di tempi convenienti)
tab=pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/trasformate_fourier/copernicus_PG_selected.csv')
time=tab['date']
co=tab['mean_co_ug/m3']
pm10=tab['mean_pm10_ug/m3']
pm2=tab['mean_pm2p5_ug/m3']
so2=tab['mean_so2_ug/m3']
nh3=tab['mean_nh3_ug/m3']
no2=tab['mean_no2_ug/m3']
o3=tab['mean_o3_ug/m3']

plt.figure(figsize=(12,8))
plt.plot(time, co, label='CO', color='teal')
plt.plot(time, pm10, label='PM10', color='mediumspringgreen')
plt.plot(time, pm2, label='PM2P5', color='magenta')
plt.plot(time, so2, label='SO2', color='orange')
plt.plot(time, nh3, label='NH3', color='purple')
plt.plot(time, no2, label='NO2', color='gold')
plt.plot(time, o3, label='O3', color='orchid')
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
plt.title('Spettro di potenza: CO')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Frequenze')
plt.ylabel('|c_k|^2')
plt.show()

par_co, pcov_co = optimize.curve_fit(fit, xdata=freq_co[50:len(co)//2], ydata=mod2_co[49:], p0=[3, 1], absolute_sigma=True)
print('DATA CO _ Parametri estratti dal fit: ', par_co)
fit_co=fit(freq_co[1:len(co)//2], par_co[0], par_co[1])

plt.figure(figsize=(11,5))
plt.plot(freq_co[1:len(co)//2], mod2_co, color='teal', label='Data CO')
plt.plot(freq_co[1:len(co)//2], fit_co, color='red', label='Fit_CO')
plt.title('Spettro di potenza e fit: CO')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Frequenze')
plt.ylabel('|c_k|^2')
plt.show()

#Spettro di potenza nel periodo e ragiona
plt.figure(figsize=(11,5))
plt.plot(1/freq_co[1:len(co)//2], mod2_co, color='teal')
plt.title('Spettro di potenza: CO')
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
plt.plot(time, co, label='CO', color='teal')
plt.plot(time, co_filter, label='CO smooth', color='red')
plt.legend()
plt.xlabel('Tempo giuliano')
plt.ylabel('Concentrazione ug/m3')
plt.title("Concentrazione di CO nell'atmosfera")
plt.show()



#Fai per un altro inquinante: o3
fr_o3=fft.fft(o3.values)
freq_o3=0.5*fft.fftfreq(len(o3), d=dt)
mod2_o3=abs(fr_o3[1:len(o3)//2])**2

plt.figure(figsize=(11,5))
plt.plot(freq_o3[1:len(o3)//2], mod2_o3, color='orchid')
plt.title('Spettro di potenza: O3')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Frequenze')
plt.ylabel('|c_k|^2')
plt.show()


par_o3, pcov_o3 = optimize.curve_fit(fit, xdata=freq_o3[50:len(co)//2], ydata=mod2_o3[49:], p0=[3, 1], absolute_sigma=True)
print('DATA O3 _ Parametri estratti dal fit: ', par_o3)
fit_o3=fit(freq_o3[1:len(o3)//2], par_o3[0], par_o3[1])

plt.figure(figsize=(11,5))
plt.plot(freq_o3[1:len(o3)//2], mod2_o3, color='orchid', label='Data O3')
plt.plot(freq_o3[1:len(o3)//2], fit_o3, color='green', label='Fit_O3')
plt.title('Spettro di potenza e fit: O3')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Frequenze')
plt.ylabel('|c_k|^2')
plt.show()

#Spettro di potenza nel periodo e ragiona
plt.figure(figsize=(11,5))
plt.plot(1/freq_o3[1:len(o3)//2], mod2_o3, color='orchid')
plt.title('Spettro di potenza: O3')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Periodo')
plt.ylabel('|c_k|^2')
plt.show()

#Fai maschera per estrarre andamento di lungo periodo only
fftmask_o3 = abs(fr_o3)**2 < 1e8
filter_o3 = fr_o3.copy()
filter_o3[fftmask_o3]=0
# Trasformata FFT inversa con coefficienti filtrati 
o3_filter = fft.irfft(filter_o3, n=len(o3))

plt.figure(figsize=(12,8))
plt.plot(time, o3, label='O3', color='orchid')
plt.plot(time, o3_filter, label='O3 smooth', color='green')
plt.legend()
plt.xlabel('Tempo giuliano')
plt.ylabel('Concentrazione ug/m3')
plt.title("Concentrazione di O3 nell'atmosfera")
plt.show()

#Riassunto filtraggio
plt.figure(figsize=(12,8))
plt.plot(time, co, label='CO', color='teal')
plt.plot(time, o3, label='O3', color='orchid')
plt.plot(time, co_filter, label='CO smooth', color='red')
plt.plot(time, o3_filter, label='O3 smooth', color='green')
plt.legend()
plt.xlabel('Tempo giuliano')
plt.ylabel('Contentrazione ug/m3')
plt.title("Concentrazione di sostanze nell'atmosfera: andamenti a larga scala")
plt.show()
