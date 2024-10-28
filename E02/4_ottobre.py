week=['lunedì', 'martedì', 'mercoledì', 'giovedì', 'venerdì', 'sabato', 'domenica']
ottobre_l=week[1:]+week*3+week[:4]
print('I giorni della settimana sono \n', week)
print('Il mese di ottobre 2024 in giorni è \n')
for i in range(0, len(ottobre_l)):
    print(ottobre_l[i])
    if i==5 or i==5+7 or i==5+14 or i==5+21:
        print('\n')
ottobre={}
for i in range(0,31):
    ottobre.update({i+1:ottobre_l[i]})
g=int(input('Inserisci il il numero per conoscere il giorno della settimana '))
print('Il giorno {:} di ottobre 2024 è'.format(g), ottobre[g])
