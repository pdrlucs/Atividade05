def eh_palindromo(texto):
    texto_limpo = ''.join(c.lower() for c in texto if c.isalnum())
    return texto_limpo == texto_limpo[::-1]

entrada = input("Digite uma palavra ou frase: ")
print("Sim" if eh_palindromo(entrada) else "Não")