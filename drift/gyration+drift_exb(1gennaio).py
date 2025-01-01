import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from scipy import integrate
from matplotlib import cm

'''
def em_ortho(E, B, q, m, v0_x, v0_y, v0_z, N):

    ---
    DRIFT EXB
    Simulazione nello spazio tridimiensionale della traiettoria di una particella con velocità iniziale data (v0_x, v0_y, v0_z) inserita in un campo magnetico uniforme (B: asse z) ed uno elettrico ad esso ortogonale (E: asse x).
    La particella ha carica q e massa m. Questa si muove inizialmente di moto rettilineo uniforme con la velocità iniziale data, ma la velocità si modifica opportunamente ad ogni step (N totali richiesti) a causa dell'azione svolta dai campi (estesi idealmente in tutto lo spazio). Si osservi che gli step vengono immagazzinati in una matrice, dove ogni riga rappresenta rispettivamente una dimensione x, y, z.
print('Sono stati compiuti {:} step'.format(N))
    
    CHIARIRE: A QUANTI SECONDI CORRISPONDE UNO STEP?
    CHE RUOLO ASSUME IN GENERALE UNO STEP?
    Io ho associato a t il ruolo del passo temporale
    
    OSSERVA: dato che non è specificato da nessuna parte, si ipotizza che le particelle partano tutte dallo stesso punto, coincidente con l'origine del sdr

    MA QUINDI QUAL È L'INTERVALLO DEL RANGE IN CUI DEVO INTEGRARE?
    ---

    #PARTE 1: SIMULAZIONE TRAIETTORIA CON INTEGRAZIONE
    #quantità utili
    field=E/B
    omega_c=(abs(q)*B)/m
    v_ort=np.sqrt(v0_x**2+v0_y**2)
    t=(2*np.pi)/omega_c  #tempo(s) di ogni passo
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
    zt=0

    #inizio simulazione: aggiornamento della velocità
    for j in range(0, N):
        vxi=v_ort*np.cos(omega_c*j*t)
        vyi=-(q/abs(q))*v_ort*np.sin(omega_c*j*t)
        vx=np.append(vx, vxi)
        vy=np.append(vy, vyi)
        xt=xt+vxi*j*t
        yt=yt+vyi*j*t
        zt=zt+vz[j]*t*j
        x=np.append(x, xt)
        y=np.append(y, yt)
        z=np.append(z, zt)

    #TO CHECK THE VELOCITY
    print('GRAFICI DI VELOCITÀ')
    plt.figure()
    plt.plot(vx, vy, marker='.')
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
    
    print('Sono stati compiuti {:} step'.format(N))
    step=np.array([x,y,z])
    return step
'''

def em_exb(E, B, q, m, v0_x, v0_y, v0_z, N):
    '''
    GYRATION + drift ExB (aggiunto a mano)
    '''
    #quantità utili
    field=E/B
    omega_c=(abs(q)*B)/m
    v_ort=np.sqrt(v0_x**2+v0_y**2)
    t=((2*np.pi)/omega_c)/100 #denominatore: quanti N servono per vedere un giro
    time=np.linspace(0, N*t, N)
    
    #array di velocità e di posizione
    x=np.empty(0)
    y=np.empty(0)
    y_g=np.empty(0)
    z=np.empty(0)
    vx=np.empty(0)
    vy=np.empty(0)
    vy_g=np.empty(0)
    vz=np.full(N, v0_z)
    xt=0
    yt=0
    yt_g=0

    #inizio simulazione: aggiornamento della velocità
    for j in range(0, N):
        vxi=v_ort*np.cos(omega_c*j*t)
        vyi_g=-(q/abs(q))*v_ort*np.sin(omega_c*j*t)
        vyi=-(q/abs(q))*v_ort*np.sin(omega_c*j*t)-field
        vx=np.append(vx, vxi)
        vy=np.append(vy, vyi)
        vy_g=np.append(vy_g, vyi_g)
        xt=xt+vxi*t
        yt=yt+vyi*t
        yt_g=yt_g+vyi_g*t
        x=np.append(x, xt)
        y=np.append(y, yt)
        y_g=np.append(y_g, yt_g)
    z=vz*time
        
    #TO CHECK THE VELOCITY
    print('GRAFICI DI VELOCITÀ')
    print('Velocità ortogonale')
    plt.figure(figsize=(8,8))
    plt.plot(vx, vy, marker='.', color='mediumblue', label='Drift ExB')
    plt.plot(vx, vy_g, marker='.', color='orange', label='Gyration')
    plt.legend()
    plt.title('v_ortogonale (t)')
    plt.xlabel('vx (m/s)')
    plt.ylabel('vy (m/s)')
    plt.axis('equal')
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
    ax[1].plot(time, vy, color='purple', label='Drift ExB')
    ax[1].plot(time, vy_g, color='orange', label='Gyration')
    ax[1].legend()
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
    ax.scatter(vx, vy, vz, marker='.', c=vz, cmap='plasma', label='Drift ExB')
    ax.scatter(vx, vy_g, vz, marker='.', c=vz, cmap='viridis', label='Gyration')
    ax.legend()
    ax.set_aspect('equal')
    ax.set_zlim(min(vz), max(vz))
    plt.show()

    #TO CHECK THE POSITION
    print('GRAFICI DI POSIZIONE')
    print('Proiezione ortogonale della traiettoria')
    plt.figure(figsize=(8,8))
    plt.plot(x, y, marker='.', color='black', label='Drift ExB')
    plt.plot(x, y_g, marker='.', color='orange', label='Gyration')
    plt.legend()
    plt.title('Traiettoria ortogonale (t)')
    plt.xlabel('x (m/s)')
    plt.ylabel('y (m/s)')
    plt.axis('equal')
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
    ax[1].plot(time, y, color='lightseagreen', label='Drift ExB')
    ax[1].plot(time, y_g, color='orange', label='Gyration')
    ax[1].legend()
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
    ax.scatter(x, y, z, c=time, cmap='plasma', label='Drift ExB')
    ax.plot(x, y, z, color='black', lw=0.7, label='Drift ExB')
    ax.scatter(x, y_g, z, c=time, cmap='viridis', label='Gyration')
    ax.plot(x, y_g, z, color='orange', lw=0.7, label='Gyration')
    ax.set_aspect('equal', adjustable='box')
    ax.set_zlim(min(z), max(z))
    ax.legend()
    plt.show()
    
    print('Sono stati compiuti {:} step'.format(N))
    step=np.array([x,y,z])
    return step
