n = int(input('Digite um número inteiro: '))
t = 0
for c in range(1, n + 1):
    if n % c == 0:
        t += 1
print(f'O número {n} é divisível por {t} números, ', end='')
if t == 2:
    print('portanto, é um número primo.')
else:
    print('portanto, não é um número primo.')
