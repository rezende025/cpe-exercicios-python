cateto1 = float(input("Valor do cateto 1: "))
cateto2 = float(input("Valor do cateto 2: "))

# Calcula a soma dos quadrados e eleva a 0.5 para extrair a raiz quadrada
hipotenusa = (cateto1**2 + cateto2**2) ** 0.5

print(f"A hipotenusa é: {hipotenusa:.2f}")
