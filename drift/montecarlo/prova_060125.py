import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

''' ---------- MODULI ---------- '''

def exb(v, t, b, Q, e, M):
    dvxdt=(Q/M)*(v[1]*b+e)
    dvydt=-(Q/M)*v[0]*b
    dvzdt=0
    dvdt = (dvxdt, dvydt, dvzdt)
    return dvdt

def grad(v, t, b, Q, gradB, M, omega):
    vort=np.sqrt(v[0]**2+v[1]**2)
    dvxdt=(Q/M)*v[1]*b
    dvydt=-(Q/M)*v[0]*b-(Q/abs(2*Q*omega))*Q*gradB*vort**2
    '''
    dvxdt=0
    dvydt=-(Q/abs(2*Q*omega))*Q*gradB*vort**2
    '''
    dvzdt=0
    dvdt = (dvxdt, dvydt, dvzdt)
    return dvdt

def drift_exb(E, B, vx_0, vy_0, vz_0, N):
    #elettrone
    m=9.1093*10**(-31)
    q=-1.602*10**(-19)
    omega_c=(abs(q)*B)/m
    
    v0=[vx_0, vy_0, vz_0]
    t=((2*np.pi)/omega_c)/100
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


def drift_grad(dB, B, vx_0, vy_0, vz_0, N):
    #elettrone
    m=9.1093*10**(-31)
    q=-1.602*10**(-19)
    omega_c=(abs(q)*B)/m
    
    v0=[vx_0, vy_0, vz_0]
    t=((2*np.pi)/omega_c)/100
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



''' ---------- SCRIPT ---------- '''
np.random.seed(25500)  #riproducibilità esperimento
N=int(input('Inserire il numero di step compiuti dalla particella: '))

#PARTE 0: una particella
E=3000
B=0.007
dB=600*10**5
v0_x=2*10**6
v0_y=3*10**5
v0_z=5*10**2

drift_exb_0=drift_exb(E, B, v0_x, v0_y, v0_z, N)
drift_grad_0=drift_grad(dB, B, v0_x, v0_y, v0_z, N)  #PROBLEMA DA RISOLVERE

print('Visualizzazione traiettoria della particella')
fig = plt.figure(figsize = (10, 10))
ax = fig.add_subplot(projection = '3d')
ax.set_title("Traiettoria tridimensionale", fontsize = 20)
ax.set_xlabel("x (m)", fontsize = 16)
ax.set_ylabel("y (m)", fontsize = 16)
ax.set_zlabel("z (m)", fontsize = 16)
ax.plot(drift_exb_0[0], drift_exb_0[1], drift_exb_0[2], color='royalblue', label='Drift ExB')
#ax.plot(drift_grad_0[0], drift_grad_0[1], drift_grad_0[2], color='orangered', label='Drift gradB')
ax.legend()
ax.set_aspect('equal', adjustable='box')
ax.set_zlim(min(drift_exb_0[2]), max(drift_exb_0[2]))
plt.show()



#PARTE 1: set di particelle con random velocità iniziale
p=int(input('Quante particelle si desidera generare? '))

p_v0=np.empty((0,3))  #array delle v0 random (uniformemente)
for i in range(0,p):
    p_v0=np.append(p_v0, [np.random.uniform(low=-5*10**5, high=5*10**5, size=3)], axis=0)
    #p_v0=np.append(p_v0, [np.random.normal(loc=0, scale=5*10**5,size=3)], axis=0) #normal (for fun)

p_exb=np.empty((0, N))  #particelle generate con v0
for i in range(0, p):
    p_exb=np.append(p_exb, drift_exb(E, B, p_v0[i,0], p_v0[i,1], p_v0[i,2], N), axis=0)

fig = plt.figure(figsize = (9, 9))
ax = fig.add_subplot(projection = '3d')
ax.set_title("Traiettorie tridimensionali: E={:}N/C, B={:}T".format(E,B), fontsize = 20)
ax.set_xlabel("x (m)", fontsize = 16)
ax.set_ylabel("y (m)", fontsize = 16)
ax.set_zlabel("z (m)", fontsize = 16)
for i in range(0,p*3,3):
    ax.plot(p_exb[i,:], p_exb[i+1,:], p_exb[i+2,:])
ax.set_aspect('equal', adjustable='box')
plt.show()

'''
#PARTE 2: studio statistico del drift
m=9.1093*10**(-31)
q=-1.602*10**(-19)
omega_c=(abs(q)*B)/m
t=((2*np.pi)/omega_c)/100
time=np.linspace(0, N*t, N)

def derivata(x, y, n):   #per dati rumorosi
  ris=np.empty(0)
  for j in range(int(n/2), int(len(x)-1-n/2), n):
      ris=np.append(ris, (y[int(j+n/2)]-y[int(j-n/2)])/(x[int(j+n/2)]-x[int(j-n/2)]))
  return ris

v_p_exb=np.zeros((p*3,N))
for i in range(0,p*3,3):
    v_p_exb[i]=derivata(time, p_exb[i], 4)
    v_p_exb[i+1]=derivata(time, p_exb[i+1], 4)
    v_p_exb[i+2]=derivata(time, p_exb[i+2], 4)

plt.figure()
for i in range(0,p*3,3):
    print(v_p_exb[i,:])
    plt.hist(v_p_exb[i,:], bins=50, range=(-0.0003, 0.0003), alpha=0.5)
plt.title('Istogramma')
plt.xlabel('Valori estratti', fontsize=16)
plt.ylabel('Bins', fontsize=16)
plt.show()
'''

