import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import pandas as pd
from scipy import optimize

#Estrazione dei dati e tabella
tab=pd.read_csv('Jpsimumu.csv')
print(tab)
E1=tab['E1']
px1=tab['px1']
py1=tab['py1']
pz1=tab['pz1']
pt1=tab['pt1']
E2=tab['E2']
px2=tab['px2']
py2=tab['py2']
pz2=tab['pz2']
pt2=tab['pt2']

#Calcolo dell'energia come massa invariante (formula)
def mc2(a1, b1, c1, d1, a2, b2, c2, d2):
    return np.sqrt(pow(a1+a2,2)-(pow(b1+b2,2)+pow(c1+c2,2)+pow(d1+d2,2)))

m_inv=np.empty(0)
for i in range(len(E1)):
    m_inv=np.append(m_inv, mc2(E1[i], px1[i], py1[i], pz1[i], E2[i], px2[i], py2[i], pz2[i]))
print(m_inv)

#Istogramma della massa invariante ottenuta
n, bins, p = plt.hist(m_inv, bins=100, range=(1.5, 5.5), color='teal')
plt.xlabel('Valori estratti')
plt.grid()
plt.show()

#Zoom su picco principale
n, bins, p = plt.hist(m_inv, bins=100, range=(2.9, 3.3), color='teal')
plt.xlabel('Valori estratti')
plt.grid()
plt.show()

#Fit con Gauss e polinomiale di primo grado (con pannello separato di scarti)
def fg1(x, m, sigma, A, p_1, p_0):
   return A*np.exp(-pow(x-m, 2)/(2*sigma*sigma))+p_1*x+p_0

bincenters=(bins[:-1]+bins[1:])/2
par, pcov = optimize.curve_fit(fg1, xdata=bincenters, ydata=n, sigma=np.sqrt(n), p0=[3, 0.1, 0.2, 0.1, 0.1], absolute_sigma=True)
print('Parametri estratti dal fit: ', par)

gf=len(n)-5
y_gauss=fg1(bincenters, par[0], par[1], par[2], par[3], par[4])
sqrt_err=np.power((y_gauss-n)/np.sqrt(n), 2)
chi2_1=sqrt_err.sum()
chi2r_1=chi2_1/gf
print('Chi2 ridotto di fit al primo ordine: ', chi2r_1)



fig, ax = plt.subplots(2,1, figsize=(9,6), gridspec_kw={'height_ratios': [3, 1]}, sharex=True)
fig.subplots_adjust(hspace=0)

ax[0].set_title('Fit gaussiano al primo ordine', fontsize=12)
fit1=fg1(bincenters, par[0], par[1], par[2], par[3], par[4])
ax[0].plot(bincenters, fit1, color='red', label='Fit gaussiano')
ax[0].hist(m_inv, bins=100, range=(2.9, 3.3), color='teal', label='Istogramma')
ax[0].set_ylabel('Eventi Misurati', fontsize=12)
ax[0].tick_params(axis="y", labelsize=12) 
ax[0].legend(fontsize=12, frameon=False)
ax[0].text(2.90, 500, '$\chi^2 ridotto$: {:}'.format(chi2r_1), fontsize=10, color='dimgray')

ax[1].scatter(bincenters,  (n-fit1)/np.sqrt(n), color='red')
ax[1].axhline(0, color='springgreen') 
ax[1].set_xlabel('Bins', fontsize =12)
ax[1].set_ylabel('(Dati-Fit)/Err',  fontsize =12)
ax[1].tick_params(axis="x",   labelsize=12) 
ax[1].tick_params(axis="y",   labelsize=12) 
ax[1].grid(True, axis='y')
plt.show()


#Funzione fg2 data da somma di due Gauss stessa media + polinomiale di primo grado e ripetere i passaggi precedenti
def fg2(x, m, sigma_1, sigma_2, A_2, A_1, p_1, p_0):
    return A_2*np.exp(-pow(x-m, 2)/(2*sigma_1*sigma_1))+A_1*np.exp(-pow(x-m, 2)/(2*sigma_2*sigma_2))+p_1*x+p_0

bincenters=(bins[:-1]+bins[1:])/2
par, pcov = optimize.curve_fit(fg2, xdata=bincenters, ydata=n, sigma=np.sqrt(n), p0=[3, 0.1, 0.1, 0.5, 0.5, 0.5, 0.5], absolute_sigma=True)
print('Parametri estratti dal fit: ', par)

gf=len(n)-7
y_gauss=fg2(bincenters, par[0], par[1], par[2], par[3], par[4], par[5], par[6])
sqrt_err=np.power((y_gauss-n)/np.sqrt(n), 2)
chi2_2=sqrt_err.sum()
chi2r_2=chi2_2/gf
print('Chi2 ridotto di fit al secondo ordine: ', chi2r_2)


fig, ax = plt.subplots(2,1, figsize=(9,6), gridspec_kw={'height_ratios': [3, 1]}, sharex=True)
fig.subplots_adjust(hspace=0)

ax[0].set_title('Fit gaussiano al secondo ordine', fontsize=12)
fit2=fg2(bincenters, par[0], par[1], par[2], par[3], par[4], par[5], par[6])
ax[0].plot(bincenters, fit2, color='red', label='Fit gaussiano')
ax[0].hist(m_inv, bins=100, range=(2.9, 3.3), color='teal', label='Istogramma')
ax[0].set_ylabel('Eventi Misurati', fontsize=12)
ax[0].tick_params(axis="y", labelsize=12) 
ax[0].legend(fontsize=12, frameon=False)
ax[0].text(2.90, 500, '$\chi^2$ ridotto {:}'.format(chi2r_2), fontsize=10, color='black')

ax[1].scatter(bincenters,  (n-fit2)/np.sqrt(n), color='red')
ax[1].axhline(0, color='springgreen') 
ax[1].set_xlabel('Bins', fontsize =12)
ax[1].set_ylabel('(Dati-Fit)/Err',  fontsize =12)
ax[1].tick_params(axis="x",   labelsize=12) 
ax[1].tick_params(axis="y",   labelsize=12) 
ax[1].grid(True, axis='y')
plt.show()
