n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media < 5:
    print('\033[31mReprovado.\033[m')
    print(f'Nota: {media:.2f}')
elif 6.9 > media > 5:
    print('\033[33mRecuperação.\033[m')
    print(f'Nota: {media:.2f}')
elif 10 >= media > 7:
    print('\033[32mAprovado!\033[m')
    print(f'Nota: {media:.2f}')
else:
    print('\033[31mERRO!\033[m'
          '\nVerifique as notas digitadas, nota máxima: 10'
          f'\nNotas digitadas: {n1} e {n2}')
