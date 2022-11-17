tot = 0
maioridade = 0
hmaisvelho = ''
mm = 0
for i in range(1,5):
    print(f'Pessoa número {i}')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo M/F: ')).strip().upper()
    tot += idade
    if sexo == 'M' and i == 1:
        maioridade = idade
        hmaisvelho = nome
    if idade > maioridade and sexo == 'M':
        maioridade = idade
        hmaisvelho = nome
    if sexo == 'F' and idade < 20:
        mm += 1
    print('--------------------')
media = tot / 4
print(f'Media de idade: {media:.0f}')
print(f'O homem mais velho é o {hmaisvelho} e tem {maioridade} anos')
print(f'Total de mulheres com menos de 20 anos: {mm}')
