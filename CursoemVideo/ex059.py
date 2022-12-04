primeiro = int(input('Digite o primeiro valor : '))
segundo = int(input('Digite o segundo valor: '))
opcao = 0

while opcao != 5:
    print('     [ 1 ] somar ')
    print('     [ 2 ] multiplicar ')
    print('     [ 3 ] maior ')
    print('     [ 4 ] novos números ')
    print('     [ 5 ] sair do programa ')
    opcao = int(input('>>>>>> Qual é sua opção? '))
    if opcao == 1:
        print(f'A soma dos dois números é: {primeiro + segundo}')
    elif opcao == 3:
        if primeiro > segundo:
            print(f'O maior número é o primeiro ({primeiro}).')
        elif segundo > primeiro:
            print(f'O maior número é o segundo ({segundo}).')
        else:
            print('Os números são iguais')
    elif opcao == 2:
        print(f'A multiplicação dos dois números é: {primeiro * segundo}')
    elif opcao == 4:
        primeiro = int(input('Digite novamente o primeiro número: '))
        segundo = int(input('Digite novamente o segundo número: '))
print('Programa finalizado com sucesso! Obrigado por utilizar nosso serviço.')
