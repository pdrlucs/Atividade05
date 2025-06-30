def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    return valor_conta * (porcentagem_gorjeta / 100)

valor = float(input("Digite o valor da conta: R$ "))
porcentagem = float(input("Digite a porcentagem da gorjeta: "))
gorjeta = calcular_gorjeta(valor, porcentagem)
print(f"Gorjeta: R$ {gorjeta:.2f}")