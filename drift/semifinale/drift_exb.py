import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def em_exb(E, B, q, m, v0_x, v0_y, v0_z, N):
    '''
    GYRATION + drift ExB
    Osserva: il tempo è costruito in maniera opportuna per fare cammino coerente, ma non serve al di fuori della funzione.
    '''
    #quantità utili
    field=E/B
    omega_c=(abs(q)*B)/m
    v_ort=np.sqrt(v0_x**2+(v0_y+field)**2)
    theta_x=np.arccos(v0_x/v_ort)
    t=((2*np.pi)/omega_c)/100
    time=np.linspace(0, N*t, N)
    
    #array di velocità e di posizione
    x=np.empty(0)
    y=np.empty(0)
    z=np.empty(0)
    vz=np.full(N, v0_z)
    xt=0
    yt=0
    #inizio simulazione: aggiornamento della velocità
    for j in range(0, N):        
        vxi=v_ort*np.cos(omega_c*j*t+theta_x)
        vyi=-(q/abs(q))*v_ort*np.sin(omega_c*j*t+theta_x)-field
        xt=xt+vxi*t
        yt=yt+vyi*t
        x=np.append(x, xt)
        y=np.append(y, yt)
    z=vz*time
    
    step=np.array([x,y,z])
    return step
