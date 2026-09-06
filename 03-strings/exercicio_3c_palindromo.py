texto_original = input("Digite a frase ou palavra: ")

# Limpa a string: remove espaços e joga para minúsculas
texto_limpo = texto_original.replace(" ", "").lower()

# Cria a versão invertida usando fatiamento [início:fim:passo]
texto_invertido = texto_limpo[::-1]

# Verifica a igualdade (palíndromo)
if texto_limpo == texto_invertido:
    print(f"'{texto_original}' é um palíndromo!")
else:
    print(f"'{texto_original}' não é um palíndromo.")
