n = m = cont = maior = menor = soma = 0
decisao = ''
while decisao != 'N':
    n = float(input('Digite um número: '))
    cont += 1
    soma = soma + n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    decisao = str(input('Deseja continuar? [S/N] ')).strip().upper()
m = soma / cont
print(f'Você digitou {cont} números e a média foi {m:.2f}.')
print(f'O maior número digitado foi {maior:.0f} e o menor foi {menor:.0f}.')
