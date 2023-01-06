print('Lojinha')
print('-'*40)
tot = pmil = pbrt = cont = 0
prodb = ''
while True:
    np = str(input('Nome do produto? '))
    pp = float(input('Preço R$'))
    c = str(input('Desejar continuar? [S/N]')).strip().upper()[0]
    print(' ')
    tot += pp
    cont += 1
    if pp > 1000:
        pmil += 1
    if cont == 1 or pp < pbrt:
        pbrt = pp
        prodb = np
    if c in 'N':
        break
print(f'Total da compra: R${tot:.2f}')
print(f'{pmil} produtos custam acima de R$1000.00')
print(f'O produto mais barato de seu carrinho foi {prodb} e custa R${pbrt:.2f}')
