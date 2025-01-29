import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

''' ---------- Drift EXB ---------- '''
def exb(v, t, b, Q, e, M):
    '''
    exb
    Funzione associata alla legge del moto per campo elettrico e magnetico ortogonali.
    Si esplicita la derivata della velocità per ciascuna componente.
    '''
    dvxdt=(Q/M)*(e+(v[1]*b))
    dvydt=-(Q/M)*v[0]*b
    dvzdt=0
    dvdt = (dvxdt, dvydt, dvzdt)
    return dvdt

def drift_exb(E, B, vx_0, vy_0, vz_0, N):
    '''
    drift_exb
    Funzione che restituisce sottoforma di array bidimensionale la traiettoria compiuta dalla particella
    esplicitata per ciascuna componente x, y, z in caso ci siano campo elettrico e magnetico ortogonali.
    La velocità è aggiornata sotto forma di integrale a partire dalla legge del moto,
    mentre la posizione è calcolata come fosse un moto uniforme, proporzionale alla velocità.  
    '''
    #elettrone
    m=9.1093*10**(-31)
    q=-1.602*10**(-19)
    v0=[vx_0, vy_0, vz_0]
    t=10**(-8)/30
    time=np.linspace(0, N*t, N)
    
    v=integrate.odeint(exb, v0, time, args=(B, q, E, m))
    x=np.empty(0)
    y=np.empty(0)
    z=np.empty(0)
    xt=0
    yt=0
    zt=0

    #inizio simulazione: aggiornamento della velocità
    for j in range(0, N):
        xt=xt+v[j,0]*t
        yt=yt+v[j,1]*t
        zt=zt+v[j,2]*t
        x=np.append(x, xt)
        y=np.append(y, yt)
        z=np.append(z, zt)
    
    step=np.array([x, y, z])
    return step

''' ---------- Drift gradB ---------- '''
def grad(v, t, b, Q, gradB, M, omega):
    '''
    grad
    Funzione associata alla legge del moto per campo magnetico con gradiente ortogonale.
    Si esplicita la derivata della velocità per ciascuna componente.
    '''
    vort=np.sqrt(v[0]**2+v[1]**2)
    B=b+gradB*(Q/abs(Q))*(vort/omega)*np.cos(omega*t)
    dvxdt=(Q/M)*B*v[1]
    dvydt=-(Q/M)*B*v[0]
    dvzdt=0
    dvdt = (dvxdt, dvydt, dvzdt)
    return dvdt

def drift_grad(dB, B, vx_0, vy_0, vz_0, N):
    '''
    drift_grad
    Funzione che restituisce sottoforma di array bidimensionale la traiettoria compiuta dalla particella
    esplicitata per ciascuna componente x, y, z in caso di una campo magnetico con gradiente ortogonale.
    La velocità è aggiornata sotto forma di integrale a partire dalla legge del moto,
    mentre la posizione è calcolata come fosse un moto uniforme, proporzionale alla velocità.  
    '''
    #elettrone
    m=9.1093*10**(-31)
    q=-1.602*10**(-19)
    omega_c=(abs(q)*B)/m
    v0=[vx_0, vy_0, vz_0]
    t=10**(-9)/23
    time=np.linspace(0, N*t, N)
    
    v=integrate.odeint(grad, v0, time, args=(B, q, dB, m, omega_c))
    x=np.empty(0)
    y=np.empty(0)
    z=np.empty(0)
    xt=0
    yt=0
    zt=0

    #inizio simulazione: aggiornamento della velocità
    for j in range(0, N):
        xt=xt+v[j,0]*t
        yt=yt+v[j,1]*t
        zt=zt+v[j,2]*t
        x=np.append(x, xt)
        y=np.append(y, yt)
        z=np.append(z, zt)
    
    step=np.array([x, y, z])
    return step
