s = str(input("Digite o sexo [M/F]: ")).strip().upper()[0]
while s != "M" and s != "F":
    s = str(input("Sexo inválido. Digite novamente[M/F]:")).strip().upper()[0]
print(f"Sexo registrado com sucesso. o sexo digitado foi: {s}")
