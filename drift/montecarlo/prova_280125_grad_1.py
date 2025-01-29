import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

''' ---------- MODULO ---------- '''
def grad(v, t, b, Q, gradB, M, omega, vx_0, vy_0):
    vort=np.sqrt(v[0]**2+v[1]**2)
    B=b+gradB*(Q/abs(Q))*(vort/omega)*np.cos(omega*t)
    dvxdt=(Q/M)*B*v[1]
    dvydt=-(Q/M)*B*v[0]
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
    
    v=integrate.odeint(grad, v0, time, args=(B, q, dB, m, omega_c, vx_0, vy_0))
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
p=int(input('Quante particelle si desidera generare? '))

#PARTE 0: una particella
B=0.008
dB=0.5
v0_x=2*10**6
v0_y=3*10**6
v0_z=5*10**2

drift_grad_0=drift_grad(dB, B, v0_x, v0_y, v0_z, N) 

m=9.1093*10**(-31)
q=-1.602*10**(-19)
omega_c=(abs(q)*B)/m
v_ort_2=v0_x**2+v0_y**2

print('\nConfigurazione dei campi: B={:} T, gradB={:} T/m'.format(B, dB))
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

p_v0=np.empty((0,3))  #array delle v0 random (uniformemente)
for i in range(0,p):
    p_v0=np.append(p_v0, [np.random.uniform(low=-6000000, high=6000000, size=3)], axis=0)


    
#PARTE 1.1: set di particelle con random velocità iniziale
th=-(q/abs(q))*(q*v_ort_2*dB)/(2*omega_c)
print('Drift atteso su x per gradB: ', th)

p_grad=np.empty((0, N))  #particelle generate con v0
for i in range(0, p):
    p_grad=np.append(p_grad, drift_grad(dB, B, p_v0[i,0], p_v0[i,1], p_v0[i,2], N), axis=0)

fig = plt.figure(figsize = (9, 9))
ax = fig.add_subplot(projection = '3d')
ax.set_title("Traiettorie tridimensionali: B={:}T; gradB={:}T/m".format(B, dB), fontsize = 20)
ax.set_xlabel("x (m)", fontsize = 16)
ax.set_ylabel("y (m)", fontsize = 16)
ax.set_zlabel("z (m)", fontsize = 16)
for i in range(0,p*3,3):
    ax.plot(p_grad[i,:], p_grad[i+1,:], p_grad[i+2,:])
ax.set_aspect('equal', adjustable='box')
plt.show()


#PARTE 1.2: studio statistico del drift
t=10**(-8)/30
dt=N*t

vm_c_grad=np.empty((0, 3))       #velocità medie exb in componenti
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

vm_grad=np.empty(0)           #modulo velocità medie exb di drift xy
vm_y=np.empty(0)
vm_x=np.empty(0)
for i in range(0,p):
    vm=np.sqrt(vm_c_grad[i,0]**2+vm_c_grad[i,1]**2)  
    vm_grad=np.append(vm_grad, vm)
    vm_y=np.append(vm_y, vm_c_grad[i,1])
    vm_x=np.append(vm_x, vm_c_grad[i,0])

fig, ax=plt.subplots(1,3, figsize=(18,8))
fig.suptitle('Istogrammi di velocità medie di drift', fontsize=35)
ax[0].set_title('x', fontsize=25)
ax[0].hist(vm_x, bins=25, range=(min(vm_x), max(vm_x)), color='yellow')
ax[0].scatter(th, 1, color='green')
ax[0].set_xlabel('Bins', fontsize=23)
ax[0].set_ylabel('Valori estratti', fontsize=23)
ax[1].set_title('y', fontsize=25)
ax[1].hist(vm_y, bins=25, range=(min(vm_y), max(vm_y)), color='cornflowerblue')
ax[1].scatter(0, 1, color='green')
ax[1].set_xlabel('Bins', fontsize=23)
ax[2].set_title('xy', fontsize=25)
ax[2].hist(vm_grad, bins=25, range=(min(vm_grad), max(vm_grad)), color='red')
ax[2].scatter(th, 1, color='green')
ax[2].set_xlabel('Bins', fontsize=23)
plt.show()

plt.figure(figsize = (9, 10))
plt.hist(vm_grad, bins=25, range=(min(vm_grad), max(vm_grad)), color='red', alpha=0.5, label='xy')
plt.hist(abs(vm_x), bins=25, range=(min(abs(vm_x)), max(abs(vm_x))), color='cornflowerblue', alpha=0.5, label='x')
plt.scatter(th, 1, color='green')
plt.title('Istogrammi moduli di velocità medie di drift')
plt.legend()
plt.ylabel('Valori estratti', fontsize=16)
plt.xlabel('Bins', fontsize=16)
plt.show()







#PARTE 2.1: set di particelle con random velocità iniziale
B=0.3
dB=0.001
print('\nConfigurazione dei campi: B={:} T, gradB={:} T/m'.format(B, dB))
th=-(q/abs(q))*(q*v_ort_2*dB)/(2*omega_c)
print('Drift atteso su x per gradB: ', th)

p_grad=np.empty((0, N))  #particelle generate con v0
for i in range(0, p):
    p_grad=np.append(p_grad, drift_grad(dB, B, p_v0[i,0], p_v0[i,1], p_v0[i,2], N), axis=0)

fig = plt.figure(figsize = (9, 9))
ax = fig.add_subplot(projection = '3d')
ax.set_title("Traiettorie tridimensionali: B={:}T; gradB={:}T/m".format(B, dB), fontsize = 20)
ax.set_xlabel("x (m)", fontsize = 16)
ax.set_ylabel("y (m)", fontsize = 16)
ax.set_zlabel("z (m)", fontsize = 16)
for i in range(0,p*3,3):
    ax.plot(p_grad[i,:], p_grad[i+1,:], p_grad[i+2,:])
ax.set_aspect('equal', adjustable='box')
plt.show()


#PARTE 2.2: studio statistico del drift
t=10**(-8)/30
dt=N*t

vm_c_grad=np.empty((0, 3))       #velocità medie exb in componenti
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

vm_grad=np.empty(0)           #modulo velocità medie exb di drift xy
vm_y=np.empty(0)
vm_x=np.empty(0)
for i in range(0,p):
    vm=np.sqrt(vm_c_grad[i,0]**2+vm_c_grad[i,1]**2)  
    vm_grad=np.append(vm_grad, vm)
    vm_y=np.append(vm_y, vm_c_grad[i,1])
    vm_x=np.append(vm_x, vm_c_grad[i,0])

fig, ax=plt.subplots(1,3, figsize=(18,8))
fig.suptitle('Istogrammi di velocità medie di drift', fontsize=35)
ax[0].set_title('x', fontsize=25)
ax[0].hist(vm_x, bins=25, range=(min(vm_x), max(vm_x)), color='yellow')
ax[0].scatter(th, 1, color='green')
ax[0].set_xlabel('Bins', fontsize=23)
ax[0].set_ylabel('Valori estratti', fontsize=23)
ax[1].set_title('y', fontsize=25)
ax[1].hist(vm_y, bins=25, range=(min(vm_y), max(vm_y)), color='cornflowerblue')
ax[1].scatter(0, 1, color='green')
ax[1].set_xlabel('Bins', fontsize=23)
ax[2].set_title('xy', fontsize=25)
ax[2].hist(vm_grad, bins=25, range=(min(vm_grad), max(vm_grad)), color='red')
ax[2].scatter(th, 1, color='green')
ax[2].set_xlabel('Bins', fontsize=23)
plt.show()

plt.figure(figsize = (9, 10))
plt.hist(vm_grad, bins=25, range=(min(vm_grad), max(vm_grad)), color='red', alpha=0.5, label='xy')
plt.hist(abs(vm_x), bins=25, range=(min(abs(vm_x)), max(abs(vm_x))), color='cornflowerblue', alpha=0.5, label='x')
plt.scatter(th, 1, color='green')
plt.title('Istogrammi moduli di velocità medie di drift')
plt.legend()
plt.ylabel('Valori estratti', fontsize=16)
plt.xlabel('Bins', fontsize=16)
plt.show()







#PARTE 3.1: set di particelle con random velocità iniziale
B=0.0009
dB=0.02
print('\nConfigurazione dei campi: B={:} T, gradB={:} T/m'.format(B, dB))
th=-(q/abs(q))*(q*v_ort_2*dB)/(2*omega_c)
print('Drift atteso su x per gradB: ', th)

p_grad=np.empty((0, N))  #particelle generate con v0
for i in range(0, p):
    p_grad=np.append(p_grad, drift_grad(dB, B, p_v0[i,0], p_v0[i,1], p_v0[i,2], N), axis=0)

fig = plt.figure(figsize = (9, 9))
ax = fig.add_subplot(projection = '3d')
ax.set_title("Traiettorie tridimensionali: B={:}T; gradB={:}T/m".format(B, dB), fontsize = 20)
ax.set_xlabel("x (m)", fontsize = 16)
ax.set_ylabel("y (m)", fontsize = 16)
ax.set_zlabel("z (m)", fontsize = 16)
for i in range(0,p*3,3):
    ax.plot(p_grad[i,:], p_grad[i+1,:], p_grad[i+2,:])
ax.set_aspect('equal', adjustable='box')
plt.show()


#PARTE 3.2: studio statistico del drift
t=10**(-8)/30
dt=N*t

vm_c_grad=np.empty((0, 3))       #velocità medie exb in componenti
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

vm_grad=np.empty(0)           #modulo velocità medie exb di drift xy
vm_y=np.empty(0)
vm_x=np.empty(0)
for i in range(0,p):
    vm=np.sqrt(vm_c_grad[i,0]**2+vm_c_grad[i,1]**2)  
    vm_grad=np.append(vm_grad, vm)
    vm_y=np.append(vm_y, vm_c_grad[i,1])
    vm_x=np.append(vm_x, vm_c_grad[i,0])

fig, ax=plt.subplots(1,3, figsize=(18,8))
fig.suptitle('Istogrammi di velocità medie di drift', fontsize=35)
ax[0].set_title('x', fontsize=25)
ax[0].hist(vm_x, bins=25, range=(min(vm_x), max(vm_x)), color='yellow')
ax[0].scatter(th, 1, color='green')
ax[0].set_xlabel('Bins', fontsize=23)
ax[0].set_ylabel('Valori estratti', fontsize=23)
ax[1].set_title('y', fontsize=25)
ax[1].hist(vm_y, bins=25, range=(min(vm_y), max(vm_y)), color='cornflowerblue')
ax[1].scatter(0, 1, color='green')
ax[1].set_xlabel('Bins', fontsize=23)
ax[2].set_title('xy', fontsize=25)
ax[2].hist(vm_grad, bins=25, range=(min(vm_grad), max(vm_grad)), color='red')
ax[2].scatter(th, 1, color='green')
ax[2].set_xlabel('Bins', fontsize=23)
plt.show()

plt.figure(figsize = (9, 10))
plt.hist(vm_grad, bins=25, range=(min(vm_grad), max(vm_grad)), color='red', alpha=0.5, label='xy')
plt.hist(abs(vm_x), bins=25, range=(min(abs(vm_x)), max(abs(vm_x))), color='cornflowerblue', alpha=0.5, label='x')
plt.scatter(th, 1, color='green')
plt.title('Istogrammi moduli di velocità medie di drift')
plt.legend()
plt.ylabel('Valori estratti', fontsize=16)
plt.xlabel('Bins', fontsize=16)
plt.show()

