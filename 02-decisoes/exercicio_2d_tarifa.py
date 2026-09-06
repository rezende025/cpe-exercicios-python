km = float(input("Distância em km: "))
total = 0.0

if km <= 0:
    print("Distância inválida.")
else:
    # 1ª Faixa (até 50 km)
    if km <= 50:
        total = km * 1.75
    # 2ª Faixa (de 51 até 150 km) - cobra-se os 50 iniciais mais o excedente
    elif km <= 150:
        total = (50 * 1.75) + ((km - 50) * 1.65)
    # 3ª Faixa (acima de 150 km)
    else:
        total = (50 * 1.75) + (100 * 1.65) + ((km - 150) * 1.50)

    # Regra da taxa mínima
    if total < 30.0:
        total = 30.0

    # Regra do desconto (5% equivale a multiplicar por 0.95)
    if km > 300:
        total = total * 0.95

    print(f"Valor total a pagar: R$ {total:.2f}")
