soma = 0
cont = 0
print('=-'*30)
print('Contador de números pares, digite somente números pares.')
print('=-'*30)
for c in range(1, 7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'Foi digitado {cont} número(s) par(es) e a soma de tudo é igual a {soma}.')
