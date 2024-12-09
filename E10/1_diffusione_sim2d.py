'''
Random Walk
Però siamo in due dimensioni, per cui si deve scegliere la direzione del passo attraverolìangolo generato randomicamente.
Bisogna fare funzione che. data lunghezza passo e numero passi, faccia due array che dice di quanto mi sono spostata su y e su x a partire dall'origine.
Così si conosce la coordinata dopo un numero rbitrario di passi.
A. Questo deve essere un modulo, si crei uno script che usi il modulo per 5 random walker per 1000 passi.
B. Nuovo grafico 2d per fare 100 random walker con 10, 100 e 1000 passi.
C. Fai grafico con due pannelli: uno è A e l'altro la distanza raggiunta quadratica.

'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import probsim as pp

#Estrazione delle coordinate dela random walk: 1000
step=int(input('Si scelga quanto sono lunghi i passi: '))
X=np.empty((5, 1000))
Y=np.empty((5, 1000))
P=np.empty((5, 1000))
D=np.empty((5, 1000))
for i in range(0, 5):
    x,y, p, d=pp.rw2d_sim(step, 1000)
    for j in range(0, 1000):
        X[i][j]= x[j]
        Y[i][j]= y[j]
        P[i][j]= p[j]
        D[i][j]= d[j]

plt.figure(figsize=(10,10))
plt.title('Simulazione di random walk: N=1000')
for i in range(0, 5):
    plt.plot(X[i], Y[i], label='Random Walk {:}'.format(i), alpha=0.6)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

#100 random walk dopo 10, 100, 1000 passi
X1=np.empty((100, 10))
Y1=np.empty((100, 10))
for i in range(0, 100):
    x1,y1, p1, d1=pp.rw2d_sim(step, 10)
    for j in range(0, 10):
        X1[i][j]= x1[j]
        Y1[i][j]= y1[j]

X2=np.empty((100, 100))
Y2=np.empty((100, 100))
for i in range(0, 100):
    x2,y2, p2, d2=pp.rw2d_sim(step, 100)
    for j in range(0, 100):
        X2[i][j]= x2[j]
        Y2[i][j]= y2[j]

X3=np.empty((100, 1000))
Y3=np.empty((100, 1000))
for i in range(0, 100):
    x3,y3, p3, d3=pp.rw2d_sim(step, 1000)
    for j in range(0, 1000):
        X3[i][j]= x3[j]
        Y3[i][j]= y3[j]

fig, ax = plt.subplots(1,3, figsize=(21, 7))
ax[0].set_title('Simulazione di random walk: N=10')
for i in range(0, 100):
    ax[0].plot(X1[i], Y1[i], alpha=0.6)
ax[0].set_xlabel('x')
ax[0].set_ylabel('y')
ax[1].set_title('Simulazione di random walk: N=100')
for i in range(0, 100):
    ax[1].plot(X2[i], Y2[i], alpha=0.6)
ax[1].set_xlabel('x')
ax[1].set_ylabel('y')
ax[2].set_title('Simulazione di random walk: N=1000')
for i in range(0, 100):
    ax[2].plot(X3[i], Y3[i], alpha=0.6)
ax[2].set_xlabel('x')
ax[2].set_ylabel('y')
plt.show()

plt.figure(figsize=(10,10))
plt.title('Simulazione di random walk')
for i in range(0, 100):
    plt.plot(X3[i], Y3[i], alpha=0.3, color='black')
    plt.plot(X2[i], Y2[i], alpha=0.4, color='cornflowerblue')
    plt.plot(X1[i], Y1[i], alpha=0.5, color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#Doppio pannello

fig, ax = plt.subplots(1,2, figsize=(21, 7))
ax[0].set_title('Simulazione di random walk: N=1000')
for i in range(0, 5):
    ax[0].plot(X[i], Y[i], alpha=0.6)
ax[0].set_xlabel('x')
ax[0].set_ylabel('y')
ax[1].set_title('Andamento della distanza: N=1000')
for i in range(0, 5):
    ax[1].plot(P[i], D[i], alpha=0.6)
ax[1].set_xlabel('Step')
ax[1].set_ylabel('Distanza r')
plt.show()
