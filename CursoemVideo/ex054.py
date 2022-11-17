from datetime import date
hj = date.today().year
maior = 0
menor = 0
for p in range(1, 8):
    nasc = int(input(f'Digite o ano de nascimento da {p}ª pessoa: '))
    idade = hj - nasc
    print(f'A pessoa tem {idade} anos.')
    if idade > 18:
        print('Maior de idade')
        maior += 1
    else:
        print('Menor de idade')
        menor += 1
print(f'Há {maior} pessoas maior de idade e {menor} pessoas menor.')
