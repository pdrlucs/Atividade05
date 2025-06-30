def calcular_desconto(preco, desconto_percentual):
    desconto = preco * (desconto_percentual / 100)
    preco_final = preco - desconto
    return round(preco_final, 2)

preco = float(input("Preço do produto: R$ "))
desconto = float(input("Desconto em %: "))
print(f"Preço final com desconto: R$ {calcular_desconto(preco, desconto):.2f}")