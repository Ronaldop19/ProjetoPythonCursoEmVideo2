while True:
    n = int(input('Digite um número para ver sua tabuada (zero ou menor para interromper): '))
    if n <= 0:
        break
    print('_'*35)
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('_'*35)
print('*'*35)
print('Programa finalizado com sucesso')
