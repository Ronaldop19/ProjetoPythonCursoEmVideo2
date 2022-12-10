n = cont = soma = 0
n = int(input('Digite um número (999 para parar): '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número (999 para parar): '))
print(f'Foram somados {cont} números e o seu total é de {soma}.')
