print('=' * 30)
print(f'Banco')
print('=' * 30)
valor = int(input('Qual valor você deseja sacar? R$'))
total = valor
cont = 0
i = 50
while True:
    if total >= i:
        total -= i
        cont += 1
    else:
        if cont > 0:
            print(f'Total de {cont} cédulas de R${i}')
        if i == 50:
            i = 20
        elif i == 20:
            i = 10
        elif i == 10:
            i = 1
        cont = 0
        if total == 0:
            break

print('Saque realizado com sucesso!')
