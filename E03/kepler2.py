import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

tab=pd.read_csv('exoplanets.csv', comment='#')
print(tab)

#Stampo nome delle colonne
print(tab.columns)

#Estraggo contenuto dela datafame
df=tab.iloc[156:234]
print(df)

#Grafico logaritmico massaVSperiodoorbitale
m=tab['pl_bmassj']
t=tab['pl_orbper']
plt.scatter(t, m, color='lime')
plt.xscale('log')
plt.yscale('log')
#metodo alternativo:   plt.scatter(np.log(t),np.log(m), color='lime')
plt.xlabel('Periodo orbitale (log_giorni)')
plt.ylabel('Massa (log_Jm)')
plt.title('1. Andamento della massa dipendentemente dal periodo orbitale')
plt.show()

#Grafico logaritmico r2max/mVSperiodoorbitale
y=(tab['pl_orbsmax']**2)/tab['st_mass']
plt.scatter(t,y, color='magenta')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Periodo orbitale (log_giorni)')
plt.ylabel('Rmax^2/m (log_au)')
plt.title('2. Andamento Rmax^2/m dipendentemente dal periodo orbitale')
plt.show()

#Grafico selezionando metodo di scoperta
eso1=tab.loc[(tab['discoverymethod']=='Transit')]
eso1m=eso1['pl_bmassj']
eso1t=eso1['pl_orbper']

eso2=tab.loc[(tab['discoverymethod']=='Radial Velocity')]
eso2m=eso2['pl_bmassj']
eso2t=eso2['pl_orbper']

plt.scatter(eso1t,eso1m, label='Transit', alpha=0.2, color='red')
plt.scatter(eso1t,eso1m, label='Radial Velocity', alpha=0.2, color='lightblue')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.xlabel('Periodo orbitale (log_giorni)')
plt.ylabel('m (log_Jm)')
plt.title('3. Andamento della massa dipendentemente dal periodo orbitale, selezonamento su metodo di scoperta')
plt.show()

#Grafico istogramma per dati precedenti di massa
n, bis, p = plt.hist(eso1m, bins=100, range=(0, 400), color='gold', alpha=0.3)
n, bis, p = plt.hist(eso2m, bins=100, range=(0, 400), color='red', alpha=0.3)
plt.xlabel('valore estratto ', fontsize=16)
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()
