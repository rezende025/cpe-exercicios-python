import math

a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

if a + b > c and a + c > b and b + c > a:
    p = (a + b + c) / 2
    # math.sqrt() é a função específica para raízes quadradas
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(f"Área do triângulo: {area:.2f}")
else:
    print("Os valores informados NÃO formam um triângulo.")
