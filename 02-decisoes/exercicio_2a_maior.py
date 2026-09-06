v1 = float(input("Valor 1: "))
v2 = float(input("Valor 2: "))
v3 = float(input("Valor 3: "))

# Coloca os valores numa lista e os organiza do menor para o maior
valores_ordenados = sorted([v1, v2, v3])

# O maior é o último elemento (índice 2)
maior = valores_ordenados[2]
# O intermediário é o elemento do meio (índice 1)
intermediario = valores_ordenados[1]

print(f"O maior valor é: {maior}")
print(f"O valor intermediário é: {intermediario}")
