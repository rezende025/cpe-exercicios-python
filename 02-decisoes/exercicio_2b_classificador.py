# O enunciado pede especificamente um número inteiro
n = int(input("Digite um número inteiro: "))

# Classificação principal
if n > 0:
    print("O número é positivo.")
elif n < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

# Condição adicional: se não for zero, verifica se é par
if n != 0:
    if n % 2 == 0:
        print("Também é um número par.")
    else:
        print("Também é um número ímpar.")
