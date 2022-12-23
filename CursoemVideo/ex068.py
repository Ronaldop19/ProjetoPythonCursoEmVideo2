from random import randint
print('~'*25)
print('Jogo do PAR ou ÍMPAR')
print('~'*25)
v = 0
while True:
     tipo = ' '
     player = int(input('Digite sua escolha: '))
     pc = randint(0, 11)
     tot = player + pc
     while tipo not in 'PI':
          tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
     print(f'Você jogou {player} e o computador jogou {pc}, o total foi de {tot}')
     if tipo == 'P':
          if tot % 2 == 0:
             print('Você ganhou!')
             v += 1
          else:
            print('Você perdeu.')
            break
     if tipo == 'I':
          if tot % 2 != 0:
            print('Você ganhou!')
            v += 1
          else:
            print('Você perdeu.')
            break
     print('Vamos jogar novamente!')
print(f'\033[31mGame Over!\033[m Número de \033[32mvitórias\033[m: \033[32m{v}\033[m.')
