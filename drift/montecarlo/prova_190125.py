import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

''' ---------- MODULO ---------- '''
def exb(v, t, b, Q, e, M):
    dvxdt=(Q/M)*(e+(v[1]*b))
    dvydt=-(Q/M)*v[0]*b
    dvzdt=0
    dvdt = (dvxdt, dvydt, dvzdt)
    return dvdt

def drift_exb(E, B, vx_0, vy_0, vz_0, N):
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

def drift_grad(dB, B, vx_0, vy_0, vz_0, N):
    #elettrone
    m=9.1093*10**(-31)
    q=-1.602*10**(-19)
    omega_c=(abs(q)*B)/m
    v0=[vx_0, vy_0, vz_0]
    t=10**(-8)/30
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



''' ---------- SCRIPT EXB ---------- '''
np.random.seed(25500)  #riproducibilità esperimento
N=int(input('Inserire il numero di step compiuti dalla particella: '))

#PARTE 0: una particella
E=3000
B=0.007
v0_x=2*10**6
v0_y=3*10**5
v0_z=5*10**2

drift_exb_0=drift_exb(E, B, v0_x, v0_y, v0_z, N)
print('Drift atteso su y per EXB: ', -E/B)

print('Visualizzazione traiettoria della particella singola')
fig = plt.figure(figsize = (10, 10))
ax = fig.add_subplot(projection = '3d')
ax.set_title("Traiettoria tridimensionale", fontsize = 20)
ax.set_xlabel("x (m)", fontsize = 16)
ax.set_ylabel("y (m)", fontsize = 16)
ax.set_zlabel("z (m)", fontsize = 16)
ax.plot(drift_exb_0[0], drift_exb_0[1], drift_exb_0[2], color='royalblue', label='Drift ExB')
ax.legend()
ax.set_aspect('equal', adjustable='box')
ax.set_zlim(min(drift_exb_0[2]), max(drift_exb_0[2]))
plt.show()

#PARTE 1: set di particelle con random velocità iniziale
p=int(input('Quante particelle si desidera generare? '))

p_v0=np.empty((0,3))  #array delle v0 random (uniformemente)
for i in range(0,p):
    p_v0=np.append(p_v0, [np.random.uniform(low=-500000, high=500000, size=3)], axis=0)

p_exb=np.empty((0, N))  #particelle generate con v0
for i in range(0, p):
    p_exb=np.append(p_exb, drift_exb(E, B, p_v0[i,0], p_v0[i,1], p_v0[i,2], N), axis=0)

print('Visualizzazione traiettorie della particelle')
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


#PARTE 2: studio statistico del drift
t=10**(-8)/30
dt=N*t

vm_c_exb=np.empty((0, 3))       #velocità medie exb in componenti
for i in range(0,p*3,3):
    vm=np.array([p_exb[i,N-1], p_exb[i+1,N-1], p_exb[i+2,N-1]])/dt
    vm_c_exb=np.append(vm_c_exb, np.array([vm]), axis=0)
    
fig = plt.figure(figsize = (9, 9))
ax = fig.add_subplot(projection = '3d')
ax.set_title("Velocità medie tridimensionali", fontsize = 20)
ax.set_xlabel("vx (m/s)", fontsize = 16)
ax.set_ylabel("vy (m/s)", fontsize = 16)
ax.set_zlabel("vz (m/s)", fontsize = 16)
for i in range(0,p):
    ax.plot(np.array([0, vm_c_exb[i,0]]), np.array([0, vm_c_exb[i,1]]), np.array([0, vm_c_exb[i,2]]))
plt.show()

fig = plt.figure(figsize = (9, 9))
plt.title("Velocità medie di drift", fontsize = 20)
plt.xlabel("vx (m/s)", fontsize = 16)
plt.ylabel("vy (m/s)", fontsize = 16)
for i in range(0,p):
    plt.plot(np.array([0, vm_c_exb[i,0]]), np.array([0, vm_c_exb[i,1]]))
plt.show()

vm_exb=np.empty(0)           #modulo velocità medie exb di drift
for i in range(0,p):
    vm=np.sqrt(vm_c_exb[i,0]**2+vm_c_exb[i,1]**2)  
    vm_exb=np.append(vm_exb, vm)
print(vm_exb)

plt.figure(figsize = (9, 7))
plt.hist(vm_exb, bins=50, range=(min(vm_exb), max(vm_exb)), color='red')
plt.title('Istogramma velocità medie di drift')
plt.ylabel('Valori estratti', fontsize=16)
plt.xlabel('Bins', fontsize=16)
plt.show()



''' ---------- SCRIPT GRADB ---------- '''
np.random.seed(25500)  #riproducibilità esperimento
N=int(input('Inserire il numero di step compiuti dalla particella: '))

#PARTE 0: una particella
B=0.007
dB=6*10**7
v0_x=2*10**5
v0_y=3*10**5
v0_z=5*10**2

drift_grad_0=drift_grad(dB, B, v0_x, v0_y, v0_z, N)  #PROBLEMA DA RISOLVERE


m=9.1093*10**(-31)
q=-1.602*10**(-19)
omega_c=(abs(q)*B)/m
v_ort_2=v0_x**2+v0_y**2
print('Drift atteso su x per gradB: ', -(q/abs(q))*(q*v_ort_2*dB)/(2*omega_c))

print('Visualizzazione traiettoria della particella singola')
fig = plt.figure(figsize = (10, 10))
ax = fig.add_subplot(projection = '3d')
ax.set_title("Traiettoria tridimensionale", fontsize = 20)
ax.set_xlabel("x (m)", fontsize = 16)
ax.set_ylabel("y (m)", fontsize = 16)
ax.set_zlabel("z (m)", fontsize = 16)
ax.plot(drift_grad_0[0], drift_grad_0[1], drift_grad_0[2], color='orangered', label='Drift gradB')
ax.legend()
ax.set_aspect('equal', adjustable='box')
ax.set_zlim(min(drift_grad_0[2]), max(drift_grad_0[2]))
plt.show()

#PARTE 1: set di particelle con random velocità iniziale
p=int(input('Quante particelle si desidera generare? '))

p_v0=np.empty((0,3))  #array delle v0 random (uniformemente)
for i in range(0,p):
    p_v0=np.append(p_v0, [np.random.uniform(low=-500000, high=500000, size=3)], axis=0)

p_grad=np.empty((0, N))  #particelle generate con v0
for i in range(0, p):
    p_grad=np.append(p_grad, drift_grad(dB, B, p_v0[i,0], p_v0[i,1], p_v0[i,2], N), axis=0)

print('Visualizzazione traiettorie della particelle')
fig = plt.figure(figsize = (9, 9))
ax = fig.add_subplot(projection = '3d')
ax.set_title("Traiettorie tridimensionali: gradB={:}T/m, B={:}T".format(dB,B), fontsize = 20)
ax.set_xlabel("x (m)", fontsize = 16)
ax.set_ylabel("y (m)", fontsize = 16)
ax.set_zlabel("z (m)", fontsize = 16)
for i in range(0,p*3,3):
    ax.plot(p_grad[i,:], p_grad[i+1,:], p_grad[i+2,:])
ax.set_aspect('equal', adjustable='box')
plt.show()


#PARTE 2: studio statistico del drift
t=10**(-8)/30
dt=N*t

vm_c_grad=np.empty((0, 3))       #velocità medie gradB in componenti
for i in range(0,p*3,3):
    vm=np.array([p_grad[i,N-1], p_grad[i+1,N-1], p_grad[i+2,N-1]])/dt
    vm_c_grad=np.append(vm_c_grad, np.array([vm]), axis=0)
    
fig = plt.figure(figsize = (9, 9))
ax = fig.add_subplot(projection = '3d')
ax.set_title("Velocità medie tridimensionali", fontsize = 20)
ax.set_xlabel("vx (m/s)", fontsize = 16)
ax.set_ylabel("vy (m/s)", fontsize = 16)
ax.set_zlabel("vz (m/s)", fontsize = 16)
for i in range(0,p):
    ax.plot(np.array([0, vm_c_grad[i,0]]), np.array([0, vm_c_grad[i,1]]), np.array([0, vm_c_grad[i,2]]))
plt.show()

fig = plt.figure(figsize = (9, 9))
plt.title("Velocità medie di drift", fontsize = 20)
plt.xlabel("vx (m/s)", fontsize = 16)
plt.ylabel("vy (m/s)", fontsize = 16)
for i in range(0,p):
    plt.plot(np.array([0, vm_c_grad[i,0]]), np.array([0, vm_c_grad[i,1]]))
plt.show()

vm_grad=np.empty(0)           #modulo velocità medie gradB di drift
for i in range(0,p):
    vm=np.sqrt(vm_c_grad[i,0]**2+vm_c_grad[i,1]**2)  
    vm_grad=np.append(vm_grad, vm)
print(vm_grad)

plt.figure(figsize = (9, 7))
plt.hist(vm_grad, bins=50, range=(min(vm_grad), max(vm_grad)), color='red')
plt.title('Istogramma velocità medie di drift')
plt.ylabel('Valori estratti', fontsize=16)
plt.xlabel('Bins', fontsize=16)
plt.show()

