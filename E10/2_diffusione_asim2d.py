import numpy as np
import matplotlib.pyplot as plt
import probasim as pap

#Estrazione delle coordinate dela random walk: 1000
step=int(input('Si scelga quanto sono lunghi i passi: '))
Xa=np.empty((5, 1000))
Ya=np.empty((5, 1000))
Pa=np.empty((5, 1000))
Da=np.empty((5, 1000))
for i in range(0, 5):
    xa, ya, pa, da=pap.rw2d_asim(step, 1000)
    for j in range(0, 1000):
        Xa[i][j]= xa[j]
        Ya[i][j]= ya[j]
        Pa[i][j]= pa[j]
        Da[i][j]= da[j]

#Doppio pannello
fig, ax = plt.subplots(1,2, figsize=(21, 7))
ax[0].set_title('Simulazione di random walk asimmetrico: N=1000')
for i in range(0, 5):
    ax[0].plot(Xa[i], Ya[i], alpha=0.6)
ax[0].set_xlabel('x')
ax[0].set_ylabel('y')
ax[1].set_title('Andamento della distanza: N=1000')
for i in range(0, 5):
    ax[1].plot(Pa[i], Da[i], alpha=0.6)
ax[1].set_xlabel('Step')
ax[1].set_ylabel('Distanza r')
plt.show()
