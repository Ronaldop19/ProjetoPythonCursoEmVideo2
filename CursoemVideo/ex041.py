from datetime import date
ano = date.today().year
nasc = int(input('Digite o ano de nascimento: '))
id = ano - nasc

if id <= 9:
    print('Classificação: Mirim')
elif id <= 14:
    print('Classificação: Infantil')
elif id <= 19:
    print('Classificação: Junior')
elif id <= 25:
    print('Classificação: Sênior')
else:
    print('Classificação: Master')
