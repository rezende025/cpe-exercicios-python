# Lê ambos como strings (texto), o padrão do input()
p = input("Digite o valor (p) que será procurado: ")
q = input("Digite o valor (q) onde a busca ocorrerá: ")

# Verifica a presença usando 'in'
if p in q:
    print(f"A sequência '{p}' foi encontrada dentro de '{q}'.")
else:
    print(f"A sequência '{p}' NÃO foi encontrada em '{q}'.")
