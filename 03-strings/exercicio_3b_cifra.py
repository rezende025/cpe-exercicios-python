texto = input("Digite um texto para cifrar: ")
texto_cifrado = ""

# Analisa letra por letra
for letra in texto:
    if letra == 'a':
        texto_cifrado += 'i'
    elif letra == 'e':
        texto_cifrado += 'o'
    elif letra == 'i':
        texto_cifrado += 'u'
    else:
        # Se for qualquer outra letra, apenas copia
        texto_cifrado += letra

print(f"Texto cifrado: {texto_cifrado}")
