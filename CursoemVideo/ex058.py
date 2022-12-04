from random import randint
pc = randint(1, 10)
tentativas = 0
print('''Vamos fazer uma brincadeira?
Acabei de pensar em um número... Consegue adivinhar qual foi?
Dica: de 1 a 10.''')
acertou = False
while not acertou:
    tentativas += 1
    jogador = int(input('Vai lá, qual seu palpite? ===> '))
    if jogador == pc:
        acertou = True
    else:
        if jogador > pc:
            print('Menos. Vamos lá!')
        else:
            print('Mais. Vamos!!')

print(f'Parabéns!!! Você acertou após {tentativas} tentativas!')
