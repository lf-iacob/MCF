from datetime import datetime, timedelta
oggi=datetime.now()
print('Oggi è: {:}.{:}.{:}'.format(oggi.day, oggi.month, oggi.year))
nascita_str=input('Inserisca la data di nascita come gg.mm.aa: ')
print('La data di nascita inserita è: ', nascita_str)
nascita=datetime.strptime(nascita_str, "%d.%m.%Y")
eta=oggi-nascita
secondi=int(eta.total_seconds())
giorni=int(((secondi/60)/60)/24)
anni=int(giorni/365)
print('Lei ha vissuto circa \n {:*^12} anni \n {:*^12} giorni \n {:*^12} secondi'.format(anni, giorni, secondi))
