numero = int(input('Digite um número qualquer para visualizar seu fatorial: '))
cont = numero
fator = 1
while cont > 0:
    print(f'{cont} ', end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fator *= cont
    cont -= 1
print(f'{fator}', end='')
