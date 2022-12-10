print('Gerador de PA')
print('-=' * 10)
pt = int(input('Primeiro termo: '))
rpa = int(input('Razão da PA: '))
t = pt
cont = 1
tot = 0
adicional = 10
while adicional !=0:
    tot = tot + adicional
    while cont <= tot:
        print(f'{t} > ', end='')
        t += rpa
        cont += 1
    print('Pausa')
    adicional = int(input('Quantos termos deseja mostrar a mais (digite 0 para parar o programa): '))
print(f'Progressão finalizada com sucesso, total de termos: {tot}')
