import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Creo dataframe dei dati salvati in remoto
tab=pd.read_csv('eso_NASA.csv')

#Stampo nome delle colonne
print(tab.columns)

t=tab['TIME']
flux=tab['PDCSAP_FLUX']
fluxerr=tab['PDCSAP_FLUX_ERR']

#Grafico del flusso in funzione del tempo
plt.plot(t, flux, color='purple')
plt.xlabel('Tempo (s)')
plt.ylabel('Flusso (e/s)')
plt.title('1.Flusso in funzione del tempo')
plt.show()

#Grafico del flusso in funzione del tempo a pallini
plt.plot(t, flux, 'o', color='red')
plt.xlabel('Tempo (s)')
plt.ylabel('Flusso (e/s)')
plt.title('2.Flusso in funzione del tempo a pallini')
plt.show()

#Grafico del flusso in funzione del tempo con errori
plt.errorbar(t, flux, yerr=fluxerr, fmt='.', color='blue')
plt.xlabel('Tempo (s)')
plt.ylabel('Flusso (e/s)')
plt.title('3.Flusso in funzione del tempo con errori')
plt.savefig('Flux_error.png')
print('Immagine salvata con successo!')
plt.show()

#Grafico del flusso in funzione del tempo zoom
zoom=tab.loc[(tab['TIME']>939.15) & (tab['TIME']<939.5)]
print(zoom)
zt=zoom['TIME']
zflux=zoom['PDCSAP_FLUX']
zfluxerr=zoom['PDCSAP_FLUX_ERR']
plt.errorbar(zt, zflux, yerr=zfluxerr, fmt='.', color='blue')
plt.xlabel('Tempo (s)')
plt.ylabel('Flusso (e/s)')
plt.title('4.Flusso in funzione del tempo in zoom')
plt.show()

#Visualizzazione contemporanea grafico e zoom
fig, ax = plt.subplots(figsize=(14, 8))
plt.errorbar(t, flux, yerr=fluxerr, fmt='.', color='blue')
plt.xlabel('Tempo (s)')
plt.ylabel('Flusso (e/s)')
plt.title('5.Flusso in funzione del tempo con errori e zoom')
ins_ax=ax.inset_axes([0.7,0.7,0.3,0.3])
ins_ax.errorbar(zt, zflux)
plt.show()
