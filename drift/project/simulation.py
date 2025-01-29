import numpy as np
import matplotlib.pyplot as plt
from module import drift_exb
from module import drift_grad

np.random.seed(25500)  #riproducibilità esperimento

print('\n\n---------- Drift EXB ----------')
N=int(input('Inserire il numero di step compiuti dalla particella: '))
p=int(input('Quante particelle si desidera generare? '))
t=10**(-8)/30
dt=N*t

#PARTE 1.0: una particella
E=3000
B=0.008
v0_x=2*10**6
v0_y=3*10**5
v0_z=5*10**2

drift_exb_0=drift_exb(E, B, v0_x, v0_y, v0_z, N)

print('\nConfigurazione dei campi: E={:} N/C; B={:} T'.format(E, B))
print('Visualizzazione traiettoria della particella singola')
fig = plt.figure(figsize = (10, 10))
ax = fig.add_subplot(projection = '3d')
ax.set_title("Traiettoria tridimensionale", fontsize = 20)
ax.set_xlabel("x (m)", fontsize = 16)
ax.set_ylabel("y (m)", fontsize = 16)
ax.set_zlabel("z (m)", fontsize = 16)
ax.plot(drift_exb_0[0], drift_exb_0[1], drift_exb_0[2], color='royalblue')
ax.set_aspect('equal', adjustable='box')
ax.set_zlim(min(drift_exb_0[2]), max(drift_exb_0[2]))
plt.show()


p_v0=np.empty((0,3))  #array delle v0 random (uniformemente)
for i in range(0,p):
    p_v0=np.append(p_v0, [np.random.uniform(low=-500000, high=500000, size=3)], axis=0)


#PARTE 1.1.1: set di particelle con random velocità iniziale
print('Drift atteso su y per EXB: {:} m/s'.format(-E/B))

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


#PARTE 1.1.2: studio statistico del drift
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

vm_exb=np.empty(0)           #modulo velocità medie exb di drift xy
vm_y=np.empty(0)
vm_x=np.empty(0)
for i in range(0,p):
    vm=np.sqrt(vm_c_exb[i,0]**2+vm_c_exb[i,1]**2)  
    vm_exb=np.append(vm_exb, vm)
    vm_y=np.append(vm_y, vm_c_exb[i,1])
    vm_x=np.append(vm_x, vm_c_exb[i,0])

fig, ax=plt.subplots(1,3, figsize=(18,8))
fig.suptitle('Istogrammi di velocità medie di drift', fontsize=35)
ax[0].set_title('x', fontsize=25)
ax[0].hist(vm_x, bins=25, range=(min(vm_x), max(vm_x)), color='yellow')
ax[0].scatter(0, 1, color='green')
ax[0].set_xlabel('Bins', fontsize=23)
ax[0].set_ylabel('Valori estratti', fontsize=23)
ax[1].set_title('y', fontsize=25)
ax[1].hist(vm_y, bins=25, range=(min(vm_y), max(vm_y)), color='cornflowerblue')
ax[1].scatter(-E/B, 1, color='green')
ax[1].set_xlabel('Bins', fontsize=23)
ax[2].set_title('xy', fontsize=25)
ax[2].hist(vm_exb, bins=25, range=(min(vm_exb), max(vm_exb)), color='red')
ax[2].scatter(E/B, 1, color='green')
ax[2].set_xlabel('Bins', fontsize=23)
plt.show()


#PARTE 1.2.1: set di particelle con random velocità iniziale
E=20000
B=0.006
print('\nConfigurazione dei campi: E={:} N/C; B={:} T'.format(E, B))
print('Drift atteso su y per EXB: {:} m/s'.format(-E/B))

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


#PARTE 1.2.2: studio statistico del drift
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

vm_exb=np.empty(0)           #modulo velocità medie exb di drift xy
vm_y=np.empty(0)
vm_x=np.empty(0)
for i in range(0,p):
    vm=np.sqrt(vm_c_exb[i,0]**2+vm_c_exb[i,1]**2)  
    vm_exb=np.append(vm_exb, vm)
    vm_y=np.append(vm_y, vm_c_exb[i,1])
    vm_x=np.append(vm_x, vm_c_exb[i,0])

fig, ax=plt.subplots(1,3, figsize=(18,8))
fig.suptitle('Istogrammi di velocità medie di drift', fontsize=35)
ax[0].set_title('x', fontsize=25)
ax[0].hist(vm_x, bins=25, range=(min(vm_x), max(vm_x)), color='yellow')
ax[0].scatter(0, 1, color='green')
ax[0].set_xlabel('Bins', fontsize=23)
ax[0].set_ylabel('Valori estratti', fontsize=23)
ax[1].set_title('y', fontsize=25)
ax[1].hist(vm_y, bins=25, range=(min(vm_y), max(vm_y)), color='cornflowerblue')
ax[1].scatter(-E/B, 1, color='green')
ax[1].set_xlabel('Bins', fontsize=23)
ax[2].set_title('xy', fontsize=25)
ax[2].hist(vm_exb, bins=25, range=(min(vm_exb), max(vm_exb)), color='red')
ax[2].scatter(E/B, 1, color='green')
ax[2].set_xlabel('Bins', fontsize=23)
plt.show()


#PARTE 1.3.1: set di particelle con random velocità iniziale
E=400
B=0.005
print('\nConfigurazione dei campi: E={:} N/C; B={:} T'.format(E, B))
print('Drift atteso su y per EXB: {:} m/s'.format(-E/B))

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


#PARTE 1.3.2: studio statistico del drift
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

vm_exb=np.empty(0)           #modulo velocità medie exb di drift xy
vm_y=np.empty(0)
vm_x=np.empty(0)
for i in range(0,p):
    vm=np.sqrt(vm_c_exb[i,0]**2+vm_c_exb[i,1]**2)  
    vm_exb=np.append(vm_exb, vm)
    vm_y=np.append(vm_y, vm_c_exb[i,1])
    vm_x=np.append(vm_x, vm_c_exb[i,0])

fig, ax=plt.subplots(1,3, figsize=(18,8))
fig.suptitle('Istogrammi di velocità medie di drift', fontsize=35)
ax[0].set_title('x', fontsize=25)
ax[0].hist(vm_x, bins=25, range=(min(vm_x), max(vm_x)), color='yellow')
ax[0].scatter(0, 1, color='green')
ax[0].set_xlabel('Bins', fontsize=23)
ax[0].set_ylabel('Valori estratti', fontsize=23)
ax[1].set_title('y', fontsize=25)
ax[1].hist(vm_y, bins=25, range=(min(vm_y), max(vm_y)), color='cornflowerblue')
ax[1].scatter(-E/B, 1, color='green')
ax[1].set_xlabel('Bins', fontsize=23)
ax[2].set_title('xy', fontsize=25)
ax[2].hist(vm_exb, bins=25, range=(min(vm_exb), max(vm_exb)), color='red')
ax[2].scatter(E/B, 1, color='green')
ax[2].set_xlabel('Bins', fontsize=23)
plt.show()




print('\n\n\n---------- Drift gradB ----------')
N=int(input('Inserire il numero di step compiuti dalla particella: '))
p=int(input('Quante particelle si desidera generare? '))
t=10**(-9)/23
dt=N*t

#PARTE 2.0: una particella
#B=0.008
#dB=0.5
B=10**(-1.3)
dB=10**(-1.5)
v0_x=2*10**8
v0_y=3*10**8
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
    p_v0=np.append(p_v0, [np.random.uniform(low=-600000000, high=600000000, size=3)], axis=0)


#PARTE 2.1.1: set di particelle con random velocità iniziale
th=-(q/abs(q))*(q*v_ort_2*dB)/(2*omega_c)
print('Drift atteso su x per gradB: {:} m/s'.format(th))

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


#PARTE 2.1.2: studio statistico del drift
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


#PARTE 2.2.1: set di particelle con random velocità iniziale
#B=0.3
#dB=0.001
B=2*10**(-2)
dB=10**(-2)
print('\nConfigurazione dei campi: B={:} T, gradB={:} T/m'.format(B, dB))
th=-(q/abs(q))*(q*v_ort_2*dB)/(2*omega_c)
print('Drift atteso su x per gradB: {:} m/s'.format(th))

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


#PARTE 2.2.2: studio statistico del drift
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


#PARTE 2.3.1: set di particelle con random velocità iniziale
#B=0.0009
#dB=0.02
B=10**(-1)
dB=6*10**(-1)
print('\nConfigurazione dei campi: B={:} T, gradB={:} T/m'.format(B, dB))
th=-(q/abs(q))*(q*v_ort_2*dB)/(2*omega_c)
print('Drift atteso su x per gradB: {:} m/s'.format(th))

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


#PARTE 2.3.2: studio statistico del drift
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


print('\n\n.')
