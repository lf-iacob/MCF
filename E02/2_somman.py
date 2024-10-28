sum=0
n=input('Inserisci un numero naturale ')
for i in range(int(n)+1):
    sum+=i
print('La somma dei primi {:} numeri naturali è: '.format(n), sum)
