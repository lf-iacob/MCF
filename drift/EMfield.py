import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import integrate
from matplotlib import cm

def em_ortho(E, B, q, m, v0_x, v0_y, v0_z, N):
    '''
    DRIFT EXB
    Simulazione nello spazio tridimiensionale della traiettoria di una particella con velocità iniziale data (v0_x, v0_y, v0_z) inserita in un campo magnetico uniforme (B: asse z) ed uno elettrico ad esso ortogonale (E: asse x).
    La particella ha carica q e massa m. Questa si muove inizialmente di moto rettilineo uniforme con la velocità iniziale data, ma la velocità si modifica opportunamente ad ogni step (N totali richiesti) a causa dell'azione svolta dai campi (estesi idealmente in tutto lo spazio). Si osservi che gli step vengono immagazzinati in una matrice, dove ogni riga rappresenta rispettivamente una dimensione x, y, z.
print('Sono stati compiuti {:} step'.format(N))
    
    CHIARIRE: A QUANTI SECONDI CORRISPONDE UNO STEP?
    CHE RUOLO ASSUME IN GENERALE UNO STEP?
    Io ho associato a t il ruolo del passo temporale
    
    OSSERVA: dato che non è specificato da nessuna parte, si ipotizza che le particelle partano tutte dallo stesso punto, coincidente con l'origine del sdr

    MA QUINDI QUAL È L'INTERVALLO DEL RANGE IN CUI DEVO INTEGRARE?
    '''

    #PARTE 1: SIMULAZIONE TRAIETTORIA CON INTEGRAZIONE
    #quantità utili
    field=E/B
    omega_c=(abs(q)*B)/m
    v_ort=np.sqrt(v0_x**2+(v0_y+field)**2)
    theta_x=np.arccos(v0_x/v_ort)
    theta_y=np.arccos((v0_y+field)/v_ort)
    t=0.000001 #tempo (s) trascorso per ogni step (rendere modificabile???
    time=np.linspace(0, N*t, N)
    
    #array di velocità e di posizione
    x=np.empty(0)
    y=np.empty(0)
    z=np.empty(0)
    vx=np.array(v0_x)
    vy=np.array(v0_y)
    vz=np.full(N, v0_z)

    #inizio simulazione: aggiornamento della velocità
    for j in range(1, N):
        vx=np.append(vx, v_ort*np.cos(omega_c*j*t+theta_x))
        vy=np.append(vy, v_ort*np.cos(omega_c*j*t+theta_y)-field)
    for j in range(1, N+1):
        x=np.append(x, integrate.simpson(vx[0:j], time[0:j]))
        y=np.append(y, integrate.simpson(vy[0:j], time[0:j]))
        z=np.append(z, integrate.simpson(vz[0:j], time[0:j]))

    '''
    #TO CHECK THE VELOCITY
    print('GRAFICI DI VELOCITÀ')
    plt.figure()
    plt.scatter(vx, vy, marker='.')
    plt.title('v_ortogonale (t)')
    plt.xlabel('vx (m/s)')
    plt.ylabel('vy (m/s)')
    plt.show()

    fig = plt.figure(figsize = (9, 9))
    ax = fig.add_subplot(projection = '3d')
    ax.set_title("Velocità tridimensionale", fontsize = 20)
    ax.set_xlabel("vx (m/s)", fontsize = 16)
    ax.set_ylabel("vy (m/s)", fontsize = 16)
    ax.set_zlabel("vz (m/s)", fontsize = 16)
    ax.scatter(vx, vy, vz, marker='.', c=time, cmap='plasma')
    plt.show()
    
    print('LEGGI DI VELOCITÀ')
    fig, ax=plt.subplots(1, 3, figsize=(15,4))
    fig.suptitle('Leggi di velocità su ogni dimensione', fontsize=25, y=1)
    ax[0].set_title('VX', fontsize=15)
    ax[0].plot(time, vx, color='mediumseagreen')
    ax[0].grid(linestyle=':')
    ax[0].set_xlabel('Tempo (s)', fontsize=10)
    ax[0].set_ylabel('vx(t) (m)', fontsize=10)
    ax[1].set_title('VY', fontsize=15)
    ax[1].plot(time, vy, color='mediumvioletred')
    ax[1].grid(linestyle=':')
    ax[1].set_xlabel('Tempo (s)', fontsize=10)
    ax[1].set_ylabel('vy(t) (m)', fontsize=10)
    ax[2].set_title('VZ', fontsize=15)
    ax[2].plot(time, vz, color='orangered')
    ax[2].grid(linestyle=':')
    ax[2].set_xlabel('Tempo (s)', fontsize=10)
    ax[2].set_ylabel('vz(t) (m)', fontsize=10)
    plt.show()

    #TO CHECK THE POSITION
    print('GRAFICI DI POSIZIONE')
    plt.figure()
    plt.scatter(x, y, marker='.', c=time, cmap='plasma')
    plt.title('Traiettoria ortogonale (t)')
    plt.xlabel('x (m/s)')
    plt.ylabel('y (m/s)')
    plt.show()
    
    fig = plt.figure(figsize = (9, 9))
    ax = fig.add_subplot(projection = '3d')
    ax.set_title("Traiettoria tridimensionale", fontsize = 20)
    ax.set_xlabel("x (m)", fontsize = 16)
    ax.set_ylabel("y (m)", fontsize = 16)
    ax.set_zlabel("z (m)", fontsize = 16)
    ax.scatter(x, y, z, marker='.', c=time, cmap='plasma')
    plt.show()

    print('LEGGI ORARIE')
    fig, ax=plt.subplots(1, 3, figsize=(15,4))
    fig.suptitle('Leggi orarie su ogni dimensione', fontsize=25, y=1)
    ax[0].set_title('X', fontsize=15)
    ax[0].plot(time, x, color='mediumseagreen')
    ax[0].grid(linestyle=':')
    ax[0].set_xlabel('Tempo (s)', fontsize=10)
    ax[0].set_ylabel('x(t) (m)', fontsize=10)
    ax[1].set_title('Y', fontsize=15)
    ax[1].plot(time, y, color='mediumvioletred')
    ax[1].grid(linestyle=':')
    ax[1].set_xlabel('Tempo (s)', fontsize=10)
    ax[1].set_ylabel('y(t) (m)', fontsize=10)
    ax[2].set_title('Z', fontsize=15)
    ax[2].plot(time, z, color='orangered')
    ax[2].grid(linestyle=':')
    ax[2].set_xlabel('Tempo (s)', fontsize=10)
    ax[2].set_ylabel('z(t) (m)', fontsize=10)
    plt.show()
    '''
    
    print('Sono stati compiuti {:} step'.format(N))
    step=np.array([x,y,z])
    return step

def uniforme(E, B, v0_x, v0_y, v0_z, N):
    vx=np.empty(0)
    vy=np.empty(0)
    vz=np.empty(0)
    x=np.array([0])
    y=np.array([0])
    z=np.array([0])
    t=1 #s
    time=np.linspace(0, N*t, N)
    
    for i in range(0, N):
        vx=np.append(vx, v0_x)
        vy=np.append(vy, v0_y)
        vz=np.append(vz, v0_z)
    for i in range(1, N):
        x=np.append(x, x[i-1]+v0_x*t*N)
        y=np.append(y, y[i-1]+v0_y*N*t)
        z=np.append(z, z[i-1]+v0_z*N*t)

    print('LEGGI ORARIE')
    fig, ax=plt.subplots(1, 3, figsize=(15,4))
    fig.suptitle('Leggi orarie su ogni dimensione', fontsize=25, y=1)
    ax[0].set_title('X', fontsize=15)
    ax[0].plot(time, x, color='mediumseagreen')
    ax[0].grid(linestyle=':')
    ax[0].set_xlabel('Tempo (s)', fontsize=10)
    ax[0].set_ylabel('x(t) (m)', fontsize=10)
    ax[1].set_title('Y', fontsize=15)
    ax[1].plot(time, y, color='mediumvioletred')
    ax[1].grid(linestyle=':')
    ax[1].set_xlabel('Tempo (s)', fontsize=10)
    ax[1].set_ylabel('y(t) (m)', fontsize=10)
    ax[2].set_title('Z', fontsize=15)
    ax[2].plot(time, z, color='orangered')
    ax[2].grid(linestyle=':')
    ax[2].set_xlabel('Tempo (s)', fontsize=10)
    ax[2].set_ylabel('z(t) (m)', fontsize=10)
    plt.show()

    fig = plt.figure(figsize = (9, 9))
    ax = fig.add_subplot(projection = '3d')
    ax.set_title("Traiettoria tridimensionale", fontsize = 20)
    ax.set_xlabel("x (m)", fontsize = 16)
    ax.set_ylabel("y (m)", fontsize = 16)
    ax.set_zlabel("z (m)", fontsize = 16)
    ax.scatter(x, y, z, marker='.', c=time, cmap='plasma')
    plt.show()

    step=np.array([x, y, z])
    return step
