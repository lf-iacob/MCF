# Genero 100 valori random LCG con seed x=1, x=2, x=5
def lcg_random(x, N):
    a =    1664525
    c = 1013904223
    m = 4294967296
    xr = np.array([x%m])
    for i in range(1, N):
        newx = (a*xr[-1]+c)%m 
        xr = np.append(xr, newx)
    return xr/m
rr1 = lcg_random(1, 100)
rr2 = lcg_random(2, 100)
rr5 = lcg_random(5, 100)

# Generazione 100 valori random nell'intervallo (0-1)
ar100 = np.random.random(100)


