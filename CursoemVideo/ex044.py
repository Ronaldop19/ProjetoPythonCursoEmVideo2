loja = ' Glamour Rio '
print(f'{loja:=^40}')
valor = float(input('Digite o valor: R$'))
print(''' Formas de pagamento:
[ 1 ] À vista Dinheiro/Pix
[ 2 ] À vista no débito
[ 3 ] 2x no cartão de crédito
[ 4 ] 3x ou mais no cartão de crédito''')
n = int(input('Digite a opção: '))

if n == 1:
    total = valor - (valor * 0.1)
    print(f'Valor total: R${valor:.2f}.\n'
          f'À vista com 10% de desconto fica R${total:.2f}')
elif n == 2:
    total = valor - (valor * 0.05)
    print(f'Valor total: R${valor:.2f}.\n'
          f'Para pagamento no débito com 5% de desconto: R${total:.2f}')
elif n == 3:
    total = valor / 2
    print(f'Valor total: R${valor:.2f}.\n'
          f'Parcelamento em 2x no cartão sem juros: R${total:.2f} por parcela')
elif n == 4:
    totparcela = int(input('Digite o número de parcelas desejado (Máx de 12): '))
    total = valor + (valor * 0.2)
    parcela = total / totparcela
    print(f'Valor total: R${valor:.2f}.\n'
          f'Parcelamento no cartão de crédito em {totparcela}x: R${parcela:.2f} por parcela')
else:
    print('Opção digitada inválida, tente novamente.')
