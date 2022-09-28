n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: 
1 converter para binário
2 converter para octal
3 converter para hexadecimal''')
op = int(input('Digite a sua escolha: '))
if op == 1:
    print(f'O número {n} convertido para binário, é igual a {n:b}.')
elif op == 2:
    print(f'O número {n} convertido para octal, é igual a {n:o}.')
elif op == 3:
    print(f'O número {n} convertido para hexadecimal, é igual a {n:x}.')
else:
    print('Opção inválida.')
