import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from EMfield import em_exb
from EMprof import m_g
import random

'''
DA CORREGGERE ALLA FINE
Gli input quand richiedi all'utente di scrivere;
I commenti accanto/sopra/sotto il codice;
help() di ciascuna funzione implementata;
Togliere i print che sono stati scritti per controllare il funzionamento corretto del codice;
Correggi affinchè costo computazionale non sia alto;
Controlla che i grafici siano corretti (label, legend, titoli, unità di misura);
Richiedi le informazioni sulla particella all'utente (meti a disposizione delle particelle di default);
Scrivi tutto in una sola lingua pls.
METTI IN ORDINE TUTTO, IN BASE ALLE SUE RICHIESTE
'''

#simulo il passaggio di un elettrone
q=-1.602*10**(-19) #C
m=9.1093837015*10**(-31) #kg
B=0.0015 #T (AMS-02, secondo wikipedia)
E=6000 #N/C (numero completamente a caso)
v0_x=2*10**5
v0_y=5*10**5 #m/s (a caso, se mai "vicino" alla velocità della luce)
v0_z=1

#step da fare
N=int(input('Inserire il numero di step compiuti dalla particella: '))

#PROVA 1: uso la funzione per dritto
print(m_g(E, B, q, m, v0_x, v0_y, v0_z, N))
print(em_exb(E, B, q, m, v0_x, v0_y, v0_z, N))


'''
#PARTE 2: simulazione con velocità iniziali random
p=int(input('Quante particelle si desidera generare? '))
particles_v0=np.empty((0,3))
for i in range(0,p):
    particles_v0=np.append(particles_v0, [np.random.uniform(low=-1*10**5, high=1*10**5, size=3)], axis=0)  #in intervallo opportuno!!!!!
print('Velocità iniziali:', particles_v0)

particella=np.empty((0, N))
particella_2=np.empty((0,N))
E2=2000
B2=0.15
for i in range(0, p):
    particella=np.append(particella, em_ortho(E, B, q, m, particles_v0[i,0], particles_v0[i,1], particles_v0[i,2], N), axis=0)
    particella_2=np.append(particella_2, em_ortho(E2, B2, q, m, particles_v0[i,0], particles_v0[i,1], particles_v0[i,2], N), axis=0)
print(particella)
print(particella_2)


fig = plt.figure(figsize = (9, 9))
ax = fig.add_subplot(projection = '3d')
ax.set_title("Traiettoria tridimensionale 1: E={:}N/C, B={:}T".format(E,B), fontsize = 20)
ax.set_xlabel("x (m)", fontsize = 16)
ax.set_ylabel("y (m)", fontsize = 16)
ax.set_zlabel("z (m)", fontsize = 16)
for i in range(0,p*3,3):
    ax.scatter(particella[i,:], particella[i+1,:], particella[i+2,:], marker='.', label='Particella {:}'.format(int(i/3)))
plt.legend()
plt.show()

fig = plt.figure(figsize = (9, 9))
ax = fig.add_subplot(projection = '3d')
ax.set_title("Traiettoria tridimensionale 2: E={:}N/C, B={:}T".format(E2,B2), fontsize = 20)
ax.set_xlabel("x (m)", fontsize = 16)
ax.set_ylabel("y (m)", fontsize = 16)
ax.set_zlabel("z (m)", fontsize = 16)
for i in range(0,p*3,3):
    ax.scatter(particella_2[i,:], particella_2[i+1,:], particella_2[i+2,:], marker='.', label='Particella {:}'.format(int(i/3)))
plt.legend()
plt.show()

fig = plt.figure(figsize = (9, 9))
ax = fig.add_subplot(projection = '3d')
ax.set_title("Traiettoria tridimensionale", fontsize = 20)
ax.set_xlabel("x (m)", fontsize = 16)
ax.set_ylabel("y (m)", fontsize = 16)
ax.set_zlabel("z (m)", fontsize = 16)
for i in range(0,p*3,3):
    ax.scatter(particella[i,:], particella[i+1,:], particella[i+2,:], marker='.', color='cornflowerblue', label='1')
    ax.scatter(particella_2[i,:], particella_2[i+1,:], particella_2[i+2,:], marker='.', color='orangered', label='2')
plt.legend()
plt.show()
'''
