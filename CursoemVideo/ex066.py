s = q = 0
while True:
    print('-='*30)
    n = int(input('Digite um número (digite 999 para interromper): '))
    if n == 999:
        break
    s += n
    q += 1
print('-='*30)
print(f'Fim do programa. A quantidade de números digitados foi {q} e sua soma é de {s}.')
