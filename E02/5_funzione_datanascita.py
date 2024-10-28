from datetime import datetime, timedelta

#definisco la funzione
def calcolo_eta(nascita_str):
    nascita=datetime.strptime(nascita_str, "%d.%m.%Y")
    oggi=datetime.now()
    eta=oggi-nascita
    secondi=eta.total_seconds()
    giorni=((secondi/60)/60)/24
    anni=giorni/365
    secoli=anni/100
    return secondi, giorni, anni, secoli

str=input('Inserisca la data come gg.mm.aa: ')
unit={1:'secondi', 2:'giorni', 3:'anni', 4:'secoli'}
print('Si può calcolare età in', unit)
scelta=int(input('Si scelga unità di misura '))
print('Sono passati {:.3f} {:}'.format(calcolo_eta(str)[scelta-1], unit[scelta]))
