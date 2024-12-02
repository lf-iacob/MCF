'''
Curve luce satellite Fermi: 6 sorgenti di raggi gamma
'''

#Leggi i dati di ciascuna sorgente e dataframe
tab1=pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/trasformate_fourier/4FGL_J2202.7%2B4216_weekly_9_15_2023_mcf.csv')
tab2=pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/trasformate_fourier/4FGL_J0721.9%2B7120_weekly_9_15_2023_mcf.csv')
tab3=pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/trasformate_fourier/4FGL_J0428.6-3756_weekly_9_15_2023_mcf.csv')
tab4=pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/trasformate_fourier/4FGL_J1256.1-0547_weekly_9_15_2023_mcf.csv')
tab5=pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/trasformate_fourier/4FGL_J2253.9%2B1609_weekly_9_15_2023_mcf.csv')
tab6=pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/trasformate_fourier/4FGL_J2232.6%2B1143_weekly_9_15_2023_mcf.csv')

t1=tab1['Julian Date'].values
flux1=tab1['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'].values
t2=tab2['Julian Date'].values
flux2=tab2['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'].values
t3=tab3['Julian Date'].values
flux3=tab3['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'].values
t4=tab4['Julian Date'].values
flux4=tab4['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'].values
t5=tab5['Julian Date'].values
flux5=tab5['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'].values
t6=tab6['Julian Date'].values
flux6=tab6['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'].values

#Curve luce
plt.figure(figsize=(12,7))
plt.plot(t1, flux1, label='Sorgente 1', color='orangered', alpha=0.6)
plt.plot(t2, flux2, label='Sorgente 2', color='salmon', alpha=0.6)
plt.plot(t3, flux3, label='Sorgente 3', color='gold', alpha=0.6)
plt.plot(t4, flux4, label='Sorgente 4', color='mediumspringgreen', alpha=0.6)
plt.plot(t5, flux5, label='Sorgente 5', color='cornflowerblue', alpha=0.6)
plt.plot(t6, flux6, label='Sorgente 6', color='m', alpha=0.6)
plt.xlabel('Tempi Giuliani')
plt.ylabel('Flusso (photons cm-2 s-1)')
plt.title('Curve luce (dati satellite Fermi)')
plt.legend()
plt.grid()
plt.show()

#Visualizzazione a panneli
fig, ax = plt.subplots(2, 3, figsize=(14, 7))
ax[0,0].plot(t1, flux1, color='lightcoral')
ax[0,0].set_title('Sorgente 1')
ax[0,0].grid()
ax[0,1].plot(t2, flux2, color='lightcoral')
ax[0,1].set_title('Sorgente 2')
ax[0,1].grid()
ax[0,2].plot(t3, flux3, color='lightcoral')
ax[0,2].set_title('Sorgente 3')
ax[0,2].grid()
ax[1,0].plot(t4, flux4, color='teal')
ax[1,0].set_title('Sorgente 4')
ax[1,0].grid()
ax[1,1].plot(t5, flux5, color='teal')
ax[1,1].set_title('Sorgente 5')
ax[1,1].grid()
ax[1,2].plot(t6, flux6, color='teal')
ax[1,2].set_title('Sorgente 6')
ax[1,2].grid()
plt.show()

#Calcolo trasformate di fourier delle curve luce
fr1=fft.fft(flux1)
dt1=t1[1]-t1[0]
freq1=0.5*fft.fftfreq(len(flux1), d=dt1)[1:len(flux1)//2]
mod2_1=abs(fr1[1:len(flux1)//2])**2
mod2_1_0=abs(fr1[0]**2)
fr2=fft.fft(flux2)
dt2=t2[1]-t2[0]
freq2=0.5*fft.fftfreq(len(flux2), d=dt2)[1:len(flux2)//2]
freq2_0=0.5*fft.fftfreq(len(flux2), d=dt2)[0]
mod2_2=abs(fr2[1:len(flux2)//2])**2
mod2_2_0=abs(fr2[0]**2)
fr3=fft.fft(flux3)
dt3=t3[1]-t3[0]
freq3=0.5*fft.fftfreq(len(flux3), d=dt3)[1:len(flux3)//2]
freq3_0=0.5*fft.fftfreq(len(flux3), d=dt3)[0]
mod2_3=abs(fr3[1:len(flux3)//2])**2
mod2_3_0=abs(fr3[0]**2)
fr4=fft.fft(flux4)
dt4=t4[1]-t4[0]
freq4=0.5*fft.fftfreq(len(flux4), d=dt4)[1:len(flux4)//2]
freq4_0=0.5*fft.fftfreq(len(flux4), d=dt4)[0]
mod2_4=abs(fr4[1:len(flux4)//2])**2
mod2_4_0=abs(fr4[0]**2)
fr5=fft.fft(flux5)
dt5=t5[1]-t5[0]
freq5=0.5*fft.fftfreq(len(flux5), d=dt5)[1:len(flux5)//2]
freq5_0=0.5*fft.fftfreq(len(flux5), d=dt5)[0]
mod2_5=abs(fr5[1:len(flux5)//2])**2
mod2_5_0=abs(fr5[0]**2)
fr6=fft.fft(flux6)
dt6=t6[1]-t6[0]
freq6=0.5*fft.fftfreq(len(flux6), d=dt6)[1:len(flux6)//2]
freq6_0=0.5*fft.fftfreq(len(flux6), d=dt6)[0]
mod2_6=abs(fr6[1:len(flux6)//2])**2
mod2_6_0=abs(fr6[0]**2)

#Spettri di potenza, sovrapposti
plt.figure(figsize=(12,7))
plt.plot(freq1, mod2_1, label='Sorgente 1', color='orangered', alpha=0.7)
plt.plot(freq2, mod2_2, label='Sorgente 2', color='salmon', alpha=0.7)
plt.plot(freq3, mod2_3, label='Sorgente 3', color='gold', alpha=0.7)
plt.plot(freq4, mod2_4, label='Sorgente 4', color='mediumspringgreen', alpha=0.7)
plt.plot(freq5, mod2_5, label='Sorgente 5', color='cornflowerblue', alpha=0.7)
plt.plot(freq6, mod2_6, label='Sorgente 6', color='m', alpha=0.7)
plt.xlabel('Frequenza')
plt.ylabel('|c_k|^2')
plt.xscale('log')
plt.yscale('log')
plt.title('Spettri di potenza (dati satellite Fermi)')
plt.legend()
plt.grid()
plt.show()

#Spettri di potenza, visualizzazione a pannelli
fig, ax = plt.subplots(2, 3, figsize=(14, 7))
#fig.suptitle('Spettri di potenza', fontsize=22)
#fig.supxlabel('Frequenza', fontsize=22)
#fig.supylabel('|c_k|^2', fontsize=22)
ax[0,0].plot(freq1, mod2_1, color='lightcoral')
ax[0,0].set_title('Sorgente 1')
ax[0,0].set_xscale('log')
ax[0,0].set_yscale('log')
ax[0,0].grid()
ax[0,1].plot(freq2, mod2_2, color='lightcoral')
ax[0,1].set_title('Sorgente 2')
ax[0,1].set_xscale('log')
ax[0,1].set_yscale('log')
ax[0,1].grid()
ax[0,2].plot(freq3, mod2_3, color='lightcoral')
ax[0,2].set_title('Sorgente 3')
ax[0,2].set_xscale('log')
ax[0,2].set_yscale('log')
ax[0,2].grid()
ax[1,0].plot(freq4, mod2_4, color='teal')
ax[1,0].set_title('Sorgente 4')
ax[1,0].set_xscale('log')
ax[1,0].set_yscale('log')
ax[1,0].grid()
ax[1,1].plot(freq5, mod2_5, color='teal')
ax[1,1].set_title('Sorgente 5')
ax[1,1].set_xscale('log')
ax[1,1].set_yscale('log')
ax[1,1].grid()
ax[1,2].plot(freq6, mod2_6, color='teal')
ax[1,2].set_title('Sorgente 6')
ax[1,2].set_xscale('log')
ax[1,2].set_yscale('log')
ax[1,2].grid()
plt.show()

#Spettri di potenza sovrapposti normalizzati alla prima frequenza
plt.figure(figsize=(12,7))
mod1_n=mod2_1/mod2_1_0
mod2_n=mod2_2/mod2_2_0
mod3_n=mod2_3/mod2_3_0
mod4_n=mod2_4/mod2_4_0
mod5_n=mod2_5/mod2_5_0
mod6_n=mod2_6/mod2_6_0
plt.plot(freq1, mod1_n, label='Sorgente 1', color='orangered', alpha=0.7) #intorno a 0, già normalizzato
plt.plot(freq2, mod2_n, label='Sorgente 2', color='salmon', alpha=0.7)
plt.plot(freq3, mod3_n, label='Sorgente 3', color='gold', alpha=0.7)
plt.plot(freq4, mod4_n, label='Sorgente 4', color='mediumspringgreen', alpha=0.7)
plt.plot(freq5, mod5_n, label='Sorgente 5', color='cornflowerblue', alpha=0.7)
plt.plot(freq6, mod6_n, label='Sorgente 6', color='m', alpha=0.7)
plt.xlabel('Frequenza')
plt.ylabel('|c_k|^2')
plt.xscale('log')
plt.yscale('log')
plt.title('Spettri di potenza normalizzati (dati satellite Fermi) ')
plt.legend()
plt.grid()
plt.show()
