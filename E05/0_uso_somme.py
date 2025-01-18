import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""##Esercizio 0 - Funzioni e Moduli

Creare il file python somme.py in cui vanno definite due funzioni:
- una funzione che restituisca la somma dei primi n numeri naturali, con n da passare tramite un argomento;
- una funzione che restituisca la somma delle radici dei primi n numeri naturali, con n da passare tramite un argomento.

Creare uno script python che importi il modulo somme appena creato e ne utilizzi le funzioni

Esaminare la cartella di lavoro
"""

#MODULO: somme.py

#Funzione 1
def somman(x):
  sum=0
  for i in range (0,x+1):
    sum-sum+i
  return sum

#Funzione 2
def sommasqrt(x):
  sum=0
  for i in range (0, x+1):
    sum=sum+np.sqrt(i)
  return sum

#Funzione 3
def sommaprodotto(x):
  s=0
  p=1
  for i in range(1, x+1):
    s=s+i
    p=p*i
  return s, p

#Funzione 4
def geometrica(x, alpha=1):
  sum=0
  for i in range (1, x+1):
    sum=sum+pow(i, alpha)
  return sum

#ESERCIZIO 0_uso_somme.py

import somme as s

print('Somma dei primi n naturali')
n=input('-> Inserisca il numero naturale: ')
sum=s.somman(int (n))
print('Risultato: ', sum)
m=input('-> Inserisca il numero naturale: ')
rad=s.sommasqrt(int(m))
print('Risultato: ',rad)
