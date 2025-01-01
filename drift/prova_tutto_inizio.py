import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from driftexb import em_exb
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
E=600 #N/C (numero completamente a caso)
v0_x=2*10**5
v0_y=5*10**5 #m/s (a caso, se mai "vicino" alla velocità della luce)
v0_z=1

#step da fare
N=int(input('Inserire il numero di step compiuti dalla particella: '))

#PROVA 1: uso la funzione per dritto
p_prova=em_exb(E, B, q, m, v0_x, v0_y, v0_z, N)
t=((2*np.pi)/((abs(q)*B)/m))/100 
time=np.linspace(0, N*t, N)

fig = plt.figure(figsize = (10, 10))
ax = fig.add_subplot(projection = '3d')
ax.set_title("Traiettoria tridimensionale", fontsize = 20)
ax.set_xlabel("x (m)", fontsize = 16)
ax.set_ylabel("y (m)", fontsize = 16)
ax.set_zlabel("z (m)", fontsize = 16)
ax.scatter(p_prova[0,:], p_prova[1,:], p_prova[2,:], c=time, cmap='plasma')
ax.plot(p_prova[0,:], p_prova[1,:], p_prova[2,:], color='black', lw=0.7)
ax.set_aspect('equal', adjustable='box')
ax.set_zlim(min(p_prova[2,:]), max(p_prova[2,:]))
plt.show()


#PARTE 2: simulazione con velocità iniziali random
p=int(input('Quante particelle si desidera generare? '))
particles_v0=np.empty((0,3))
for i in range(0,p):
    particles_v0=np.append(particles_v0, [np.random.uniform(low=-5*10**5, high=5*10**5, size=3)], axis=0)
print('Velocità iniziali:', particles_v0)

particella=np.empty((0, N))
particella_2=np.empty((0,N))
E2=10
for i in range(0, p):
    particella=np.append(particella, em_exb(E, B, q, m, particles_v0[i,0], particles_v0[i,1], particles_v0[i,2], N), axis=0)
    particella_2=np.append(particella_2, em_exb(E2, B, q, m, particles_v0[i,0], particles_v0[i,1], particles_v0[i,2], N), axis=0)
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
ax.set_aspect('equal', adjustable='box')
plt.legend()
plt.show()

fig = plt.figure(figsize = (9, 9))
ax = fig.add_subplot(projection = '3d')
ax.set_title("Traiettoria tridimensionale 2: E={:}N/C, B={:}T".format(E2,B), fontsize = 20)
ax.set_xlabel("x (m)", fontsize = 16)
ax.set_ylabel("y (m)", fontsize = 16)
ax.set_zlabel("z (m)", fontsize = 16)
for i in range(0,p*3,3):
    ax.scatter(particella_2[i,:], particella_2[i+1,:], particella_2[i+2,:], marker='.', label='Particella {:}'.format(int(i/3)))
ax.set_aspect('equal', adjustable='box')
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
ax.set_aspect('equal', adjustable='box')
plt.legend()
plt.show()
