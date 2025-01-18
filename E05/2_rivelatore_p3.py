import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import reco as rc

#Leggo i dati csv
tab0=pd.read_csv('hit_times_MO.csv')
tab1=pd.read_csv('hit_times_M1.csv')
tab2=pd.read_csv('hit_times_M2.csv')
tab3=pd.read_csv('hit_times_M3.csv')

#Array di Hit per ogni file
def record(tab):
  records=np.empty(0)
  for i in range (0, len(tab['mod_id']-1)):
    add=rc.Hit(tab['mod_id'][i], tab['det_id'][i], tab['hit_time'][i])
    records=np.append(records, add)
  return records

records_0=record(tab0)
records_1=record(tab1)
records_2=record(tab2)
records_3=record(tab3)

#Riordino in base al tempo
records=np.array([records_0, records_1, records_2, records_3])
print(records)
records=np.sort(records, kind='mergesort')
print(records)

#Estraggo delta_t di reco consecutivi: 2 e 3
delta_t23=np.empty(0)
for i in range(0, len(records_0)-1):
  delta_t23=np.append(delta_t23, records_2-records_3)
print(delta_t23)

#Faccio istogramma con delta_t di reco consecutivi: 2 e 3
n, bis, p=plt.hist(delta_t23, bins=60, color='coral', edgecolor='red')
plt.title('Istogramma delta-tempi - Moduli 2-3')
plt.xlabel('Valori estratti')
plt.show()
