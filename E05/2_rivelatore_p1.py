#ESERCIZIO_PASSO1 2_rivelatore_p1.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Leggo i dati csv
tab0=pd.read_csv('hit_times_MO.csv')
tab1=pd.read_csv('hit_times_M1.csv')
tab2=pd.read_csv('hit_times_M2.csv')
tab3=pd.read_csv('hit_times_M3.csv')

#Scelgo di istogrammare il modulo 0 (-5, 5: alto, sinistra)
t0=tab0['hit_time']
n, bis, p = plt.hist(t0, bins=60, color='orchid', edgecolor='darkorchid')
plt.title('Istogramma tempi - Modulo 0')
plt.xlabel('Valori estratti')
plt.show()

#Istogramma con differenza dei tempi
dt0=np.diff(t0)
mask_zeri=dt0>0
n, bis, p=plt.hist(np.log10(dt0[mask_zeri]), bins=60, color='teal', edgecolor='black')
plt.title('Istogramma delta-tempi - Modulo 0')
plt.xlabel('Valori estratti')
plt.show()
