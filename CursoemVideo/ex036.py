casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o salário mensal do cliente: R$'))
anos = int(input('Em quantos anos gostaria de pagar o empréstimo? '))
prestacao = casa / (anos * 12)

print(f'Para pagar o imóvel de R${casa:.2f} em {anos:.0f} anos, a prestação fica'
      f' em R${prestacao:.2f} mensais.')
if prestacao > salario * 0.3:
    print('Empréstimo \033[31mnegado\033[m pela política de crédito.')
elif prestacao < salario * 0.3:
    print('Empréstimo \033[32maprovado\033[m!')
