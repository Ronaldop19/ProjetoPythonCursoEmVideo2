print('Gerador de PA')
print('-='*10)
pt = int(input('Primeiro termo: '))
rpa = int(input('Razão da PA: '))
t = pt
cont = 1
while cont <= 10:
    print(f'{t} > ', end='')
    t += rpa
    cont += 1
print('FIM')