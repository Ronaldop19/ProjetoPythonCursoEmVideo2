adultos = homens = mvinte = 0
while True:
    i = int(input('Qual a idade que deseja cadastrar? '))
    s = str(input('Qual o sexo? [M/F] ')).strip().upper()[0]
    d = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if d in 'N':
        break
    if i > 18:
        adultos += 1
    if s in 'M':
        homens += 1
    if s in 'F':
        if i < 20:
            mvinte += 1
print('Cadastro finalizado com sucesso!')
print(f'Há {adultos} pessoas maiores de 18 anos, {homens} homens foram cadastrados e {mvinte} mulheres tem menos de '
      f'vinte anos. ')
