import numpy as np

def rw2d_sim(p, N):
    #N: numero di estrazioni (passi)
    #p: lunghezza del passo
    x=np.array([0])
    y=np.array([0])
    angle=np.random.uniform(low=0, high=2*np.pi, size=N) #angolo in radianti
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
