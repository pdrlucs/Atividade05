from datetime import datetime

data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
hoje = datetime.now()
dias_vividos = (hoje - nascimento).days
print(f"Você viveu {dias_vividos} dias.")