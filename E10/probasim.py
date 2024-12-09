import numpy as np
import matplotlib.pyplot as plt

def f_sin(x):
  return (1/4)*np.sin(x/2)

#Calcolo funzione cumulative come integrale normalizzato (funzione determinata in modo analitico)
def cumsin(x):
  return (1/2)*(1-np.cos(x/2))

'''
x=np.arange(0, 101)
plt.figure()
plt.plot(x, f_sin(x), label='Funzione')
plt.plot(x, cumsin(x), label='Cumulativa')
plt.legend()
plt.xlabel('\phi')
plt.ylabel('f(\phi)')
plt.grid()
plt.show()
'''

#Inverto analiticamente la funzione cumulativa
def invcumsin(x):
  return 2*np.arccos((2*x)-1)

#Definisco la distribuzione arbitraria che ho creato con metodo cumulativo
def random_sinusoidal(N):
  x=np.random.uniform(low=0, high=1, size=N)
  y=invcumsin(x)
  return y

#Implemento la funzione per la diffusione asimmetrica
def rw2d_asim(p, N):
    #N: numero di estrazioni (passi)
    #p: lunghezza del passo
    x=np.array([0])
    y=np.array([0])
    angle=random_sinusoidal(N) #angolo in radianti
    sumx=0
    sumy=0
    dist=np.array([0])
    sumd=0
    step=np.arange(0, N)
    for i in range(0, N-1):
        xi=p*np.cos(angle[i])
        yi=p*np.sin(angle[i])
        sumx=sumx+xi
        sumy=sumy+yi
        x=np.append(x, sumx)
        y=np.append(y, sumy)
    sumd=pow(x,2)+pow(y,2)
    dist=np.append(dist, sumd)
    return x, y, step, dist
