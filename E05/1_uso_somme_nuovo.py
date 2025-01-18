import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''Esercizio 1 - Moduli e Funzioni con argomenti

Modificare il file somme.py aggiungendo:
- una funzione che restituisca la somma e il prodotto dei primi n numeri naturali, con n da passare tramite un argomento;
- una funzione che restituisca, con n da passare tramite un argomento e  da passare tramite keyword (kwargs), con valore di default pari a 1.

Modificare lo script python che importa il modulo somme in modo da utilizzare le funzioni appena create.'''

print('Somma e prodotto dei primi n naturali')
n=input('-> Inserisca il numero naturale: ')
ss=s.sommaprodotto(int(n))
print('Somma: {}, Prodotto: {}'.format(ss[0], ss[1]))

print('\n Serie speciale')
m=input('-> Inserisca il numero naturale: ')
a=input('-> Inserisca la potenza costante: ')
gg=s.geometrica(int(m))
gg1=s.geometrica(int(m), int(a))
print('Risultato di default (potenza 1): ', gg)
print('Risultato: ', gg1)
