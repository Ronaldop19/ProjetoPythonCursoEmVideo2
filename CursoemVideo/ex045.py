from random import randint
o = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Escolha uma opção:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Escolha sua arma: '))
if jogador >= 3:
    print('Jogada inválida!')
    exit()
print('-=' * 11)
print(f'Computador jogou {o[computador]}')
print(f'Jogador jogou {o[jogador]}')
print('-=' * 11)

if computador == 0:
    if jogador == 0:
        print('Empatou')
    elif jogador == 1:
        print('Jogador vence!')
    elif jogador == 2:
        print('Computador vence!')

elif computador == 1:
    if jogador == 0:
        print('Computador vence!')
    elif jogador == 1:
        print('Empatou!')
    elif jogador == 2:
        print('Jogador vence!')

elif computador == 2:
    if jogador == 0:
        print('Jogador vence!')
    elif jogador == 1:
        print('Computador vence!')
    elif jogador == 2:
        print('Empatou!')
