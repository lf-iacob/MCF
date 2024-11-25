"""
Pendolo non approssimato per piccoli angoli
Si risolve l'equazione differenzaile al secondo ordine linearizzando
con due equazioni differenziali al primo ordine: si usano gli array
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
from scipy import integrate

#Definisco l'equazione differenziale
def drdt(r, t, g, l):
    dthetadt=r[1]
    domegadt= -(g/l)*np.sin(r[0])
    return(dthetadt, domegadt)

#Definisco i parametri del sistema (condizioni iniziali incluse)
g=9.81
omega0=0 
par=np.array([[0.5,(np.pi/4)], [1,(np.pi/4)], [0.5,(np.pi/6)]])

#Risolvo equzione
time=np.linspace(0, 10, 200)
theta={}
tsol={}
for j in range(0, 3):
    xx=integrate.odeint(drdt, y0=(par[j][1], omega0), t=time, args=(g, par[j][0]))
    theta.update({j : xx})
    tsol.update({j : time})

#Grafico
plt.figure(figsize=(10,6))
plt.title('Grafici di legge oraria angolare e velocità')
for i in range(0, 3):
    plt.plot(tsol[i], theta[i], label=('Theta{:}'.format(i), 'Omega{:}'.format(i)))
plt.xlabel('Tempo [s]')
plt.ylabel('Legge del moto [UA]')
plt.legend()
plt.grid()
plt.show()
