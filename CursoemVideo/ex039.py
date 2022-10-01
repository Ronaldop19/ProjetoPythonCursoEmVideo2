nasc = int(input('Digite o ano de nascimento: '))

idade = 2022 - nasc

if idade == 18:
    print('Chegou a hora de se alistar. Compareça a junta militar.')
elif idade < 18:
    print(f'Você ainda não precisa se alistar.'
          f' Falta(m) {18 - idade} ano(s) para seu alistamento obrigatório.')
elif 99 > idade > 18:
    print(f'Você deve se alistar urgentemente! Você está {idade - 18} ano(s) atrasado.')
    print(f'Seu alistamento foi em {nasc + 18}')
else:
    print('Verifique o ano digitado.')
