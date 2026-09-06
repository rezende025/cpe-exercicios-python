palavra = input("Digite uma palavra de 5 caracteres: ")

vogais_encontradas = ""
contador = 0

# Percorre cada letra dentro da palavra digitada
for letra in palavra:
    # lower() garante que o código identifique tanto 'a' quanto 'A'
    if letra.lower() in "aeiou":
        vogais_encontradas += letra + " "
        contador += 1

print(f"Quantidade de vogais: {contador}")
print(f"Vogais presentes: {vogais_encontradas}")
