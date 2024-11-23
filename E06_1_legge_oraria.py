# -*- coding: utf-8 -*-
"""MFC_E06.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ckWkJQzChtmlbtUJUmPX6cQop4awvrIo

#MCF_E06: Integrazione e Derivazione
"""

# Import
import numpy as np
import pandas as pd
import scipy as sp
from scipy import integrate
import matplotlib.pyplot as plt

"""##1_legge_oraria.py"""

#estrazione dati
tab=pd.read_csv('https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2024/refs/heads/main/dati/integrazione_derivazione/vel_vs_time.csv')
t=tab['t']
v=tab['v']
print(tab)

#grafico velocita
plt.figure()
plt.plot(t, v, color='teal')
plt.title('Andamento della velocità')
plt.xlabel('Tempo [s]')
plt.ylabel('Velocità [m/s]')
plt.grid()
plt.show()

#integrazione
simp=np.empty(0)
for i in range(1, len(v)+1):
  integ=integrate.simpson(v[0:i], t[0:i])
  simp=np.append(simp, integ)

#grafico legge oraria
plt.figure()
plt.plot(t, simp, color='orchid')
plt.title('Legge oraria')
plt.ylabel('Legge oraria [m]')
plt.xlabel('Tempo [s]')
plt.grid()
plt.show()
