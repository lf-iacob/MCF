import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
from scipy import integrate

#Risolvere Equazione differenziale per la V_out per dato V_in
def fedo(x, t, vin, rc):
    return (vin-x)/(rc)

RC=[4, 1, 0.25]
tt=np.arange(0, 11, 0.2)

v_iniziale=int(input('Inserire valore di V_in: '))
v_out0=integrate.odeint(fedo, y0=0, t=tt, args=(v_iniziale, RC[0]))
print('Dato V_in={:} V, si ottiene una tensione V_out={:} V.'.format(v_iniziale, v_out0))

#Definizisco V_in in tempo (0,10) con V_in onda quadra
def v_in_quadro(t):
    if np.isscalar(t):
        if int(t)%2==0:
            return 1
        else:
            return -1
    else:
        ris=np.ones(len(t))
        mask=t.astype(int)%2!=0
        ris[mask]=-1
        return ris

def fedo_in(x, t, rc):
    return (v_in_quadro(t) - x)/rc

v_out={}
tsol={}
for j in range(0, 3):
    xx=integrate.odeint(fedo_in, y0=0, t=tt, args=(RC[j],))
    v_out.update({j : xx})
    tsol.update({j : tt})

#Grafico
plt.figure()
plt.title('Grafici della V_out')
plt.plot(tsol[0], v_in_quadro(tsol[0]), label='V_in', color='mediumspringgreen')
plt.plot(tsol[0], v_out[0], label='V_out, RC={:}'.format(RC[0]), color='teal')
plt.plot(tsol[1], v_out[1], label='V_out, RC={:}'.format(RC[1]), color='violet')
plt.plot(tsol[2], v_out[2], label='V_out, RC={:}'.format(RC[2]), color='salmon')
plt.xlabel('Tempo [s]')
plt.ylabel('Tensione [V]')
plt.grid()
plt.show()

#Produci file csv unico per i tre valori di RC
tab=pd.DataFrame(columns=['t', 'v_in', 'v_out0', 'v_out1', 'v_out2'])
tab['t']=tsol[0]
tab['v_in']=v_in_quadro(tsol[0])
tab['v_out0']=v_out[0]
tab['v_out1']=v_out[1]
tab['v_out2']=v_out[2]
print(tab)
tab.to_csv('tabella.csv')
