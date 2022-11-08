frase = str(input("Digite uma frase: ")).strip().upper()
p = frase.split()
j = ''.join(p)
i = ''
for letra in range(len(j) - 1, -1, -1):
    i += j[letra]
print(j, i)
if i == j:
    print('A frase digitada é um palíndromo')
else:
    print('A frase não é um palíndromo')