import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import somme as s

"""##Esercizio 0 - Funzioni e Moduli

Creare il file python somme.py in cui vanno definite due funzioni:
- una funzione che restituisca la somma dei primi n numeri naturali, con n da passare tramite un argomento;
- una funzione che restituisca la somma delle radici dei primi n numeri naturali, con n da passare tramite un argomento.

Creare uno script python che importi il modulo somme appena creato e ne utilizzi le funzioni

Esaminare la cartella di lavoro
"""

print('Somma dei primi n naturali')
n=input('-> Inserisca il numero naturale: ')
sum=s.somman(int (n))
print('Risultato: ', sum)
m=input('-> Inserisca il numero naturale: ')
rad=s.sommasqrt(int(m))
print('Risultato: ',rad)
