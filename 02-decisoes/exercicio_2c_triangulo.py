a = float(input("Tamanho do lado A: "))
b = float(input("Tamanho do lado B: "))
c = float(input("Tamanho do lado C: "))

# Verifica a desigualdade triangular para todos os lados simultaneamente
if (a + b > c) and (a + c > b) and (b + c > a):
    print("Os valores formam um triângulo válido!")
    
    # Calcula o semiperímetro
    p = (a + b + c) / 2
    
    # Fórmula de Heron (raiz quadrada extraída com potência 0.5)
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(f"A área do triângulo é: {area:.2f}")
else:
    print("Os valores informados NÃO formam um triângulo.")
