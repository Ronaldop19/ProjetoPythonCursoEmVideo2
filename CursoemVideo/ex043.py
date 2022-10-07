peso = float(input('Digite seu peso em KG: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / (altura ** 2)

print(f'O IMC é {imc:.2f}')

if imc < 18.5:
    print('Classificação: Magreza')
elif 18.5 <= imc <= 24.9:
    print('Classificação: Normal')
elif 25 <= imc <= 29.9:
    print('Classificação: Sobrepeso')
elif 30 <= imc < 39.9:
    print('Classificação: Obesidade')
else:
    print('Classificação: Obesidade grave!')
