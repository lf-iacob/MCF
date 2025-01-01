import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import integrate
from matplotlib import cm

def m_g(E, B, q, m, v0_x, v0_y, v0_z, N):
    '''
    GYRATION formula del prof Tomassetti
    '''
    #quantità utili
    omega_c=(abs(q)*B)/m
    v_ort=np.sqrt(v0_x**2+v0_y**2)
    t=((2*np.pi)/omega_c)/100 #denominatore: quanti N servono per vedere un giro
    time=np.linspace(0, N*t, N)
    
    #array di velocità e di posizione
    x=np.empty(0)
    y=np.empty(0)
    z=np.empty(0)
    vx=np.empty(0)
    vy=np.empty(0)
    vz=np.full(N, v0_z)
    xt=0
    yt=0

    #inizio simulazione: aggiornamento della velocità
    for j in range(0, N):
        vxi=v_ort*np.cos(omega_c*j*t)
        vyi=-(q/abs(q))*v_ort*np.sin(omega_c*j*t)
        vx=np.append(vx, vxi)
        vy=np.append(vy, vyi)
        xt=xt+vxi*t
        yt=yt+vyi*t
        x=np.append(x, xt)
        y=np.append(y, yt)
    z=vz*time
    '''
    INTEGRAZIONE (non necessaria aparently)
    for j in range(1, N+1):
        x=np.append(x, integrate.simpson(vx[0:j], time[0:j]))
        y=np.append(y, integrate.simpson(vy[0:j], time[0:j]))
        z=np.append(z, integrate.simpson(vz[0:j], time[0:j]))
    '''
        
    #TO CHECK THE VELOCITY
    print('GRAFICI DI VELOCITÀ')
    print('Velocità ortogonale')
    plt.figure(figsize=(8,8))
    plt.plot(vx, vy, marker='.', color='mediumblue')
    plt.title('v_ortogonale (t)')
    plt.xlabel('vx (m/s)')
    plt.ylabel('vy (m/s)')
    plt.show()
    print('Velocità: andamento nel tempo')
    fig, ax=plt.subplots(1, 3, figsize=(15,6))
    fig.suptitle('Leggi di velocità su ogni dimensione', fontsize=25, y=1)
    ax[0].set_title('VX', fontsize=15)
    ax[0].plot(time, vx, color='mediumblue')
    ax[0].grid(linestyle=':')
    ax[0].set_xlabel('Tempo (s)', fontsize=10)
    ax[0].set_ylabel('vx(t) (m)', fontsize=10)
    ax[1].set_title('VY', fontsize=15)
    ax[1].plot(time, vy, color='purple')
    ax[1].grid(linestyle=':')
    ax[1].set_xlabel('Tempo (s)', fontsize=10)
    ax[1].set_ylabel('vy(t) (m)', fontsize=10)
    ax[2].set_title('VZ', fontsize=15)
    ax[2].plot(time, vz, color='orangered')
    ax[2].grid(linestyle=':')
    ax[2].set_xlabel('Tempo (s)', fontsize=10)
    ax[2].set_ylabel('vz(t) (m)', fontsize=10)
    plt.show()
    print('Visualizzazione tridimensionale del vettore velocità')
    fig = plt.figure(figsize = (10,10))
    ax = fig.add_subplot(projection = '3d')
    ax.set_title("Velocità tridimensionale", fontsize = 20)
    ax.set_xlabel("vx (m/s)", fontsize = 16)
    ax.set_ylabel("vy (m/s)", fontsize = 16)
    ax.set_zlabel("vz (m/s)", fontsize = 16)
    ax.scatter(vx, vy, vz, marker='.', c=vz, cmap='plasma')
    plt.show()

    #TO CHECK THE POSITION
    print('GRAFICI DI POSIZIONE')
    print('Proiezione ortogonale della traiettoria')
    plt.figure(figsize=(8,8))
    plt.plot(x, y, marker='.', color='black')
    plt.title('Traiettoria ortogonale (t)')
    plt.xlabel('x (m/s)')
    plt.ylabel('y (m/s)')
    plt.show()
    print('Leggi orarie')
    fig, ax=plt.subplots(1, 3, figsize=(15,6))
    fig.suptitle('Leggi orarie', fontsize=25, y=1)
    ax[0].set_title('X', fontsize=15)
    ax[0].plot(time, x, color='mediumseagreen')
    ax[0].grid(linestyle=':')
    ax[0].set_xlabel('Tempo (s)', fontsize=10)
    ax[0].set_ylabel('x(t) (m)', fontsize=10)
    ax[1].set_title('Y', fontsize=15)
    ax[1].plot(time, y, color='lightseagreen')
    ax[1].grid(linestyle=':')
    ax[1].set_xlabel('Tempo (s)', fontsize=10)
    ax[1].set_ylabel('y(t) (m)', fontsize=10)
    ax[2].set_title('Z', fontsize=15)
    ax[2].plot(time, z, color='teal')
    ax[2].grid(linestyle=':')
    ax[2].set_xlabel('Tempo (s)', fontsize=10)
    ax[2].set_ylabel('z(t) (m)', fontsize=10)
    plt.show()
    print('Visualizzazione tridimensionale del vettore velocità')
    fig = plt.figure(figsize = (10, 10))
    ax = fig.add_subplot(projection = '3d')
    ax.set_title("Traiettoria tridimensionale", fontsize = 20)
    ax.set_xlabel("x (m)", fontsize = 16)
    ax.set_ylabel("y (m)", fontsize = 16)
    ax.set_zlabel("z (m)", fontsize = 16)
    ax.scatter(x, y, z, c=time, cmap='plasma')
    plt.plot(x, y, z, color='black', lw=0.7)
    plt.show()
    
    print('Sono stati compiuti {:} step'.format(N))
    step=np.array([x,y,z])
    return step
