def bissetriz_externa(lado_oposto, lado1, lado2):
    if lado1 == lado2:
        return None, "Erro: os lados adjacentes não podem ser iguais."

    razao = lado1 / lado2
    x = (lado_oposto * lado1) / (lado1 - lado2)
    y = x - lado_oposto

    return razao, x, y

# Exemplo de uso:
lado_oposto = float(input("Digite o comprimento do lado oposto à bissetriz externa: "))
lado1 = float(input("Digite o comprimento de um lado adjacente: "))
lado2 = float(input("Digite o comprimento do outro lado adjacente: "))

resultado = bissetriz_externa(lado_oposto, lado1, lado2)
if resultado[0] is None:
    print(resultado[1])
else:
    razao, x, y = resultado
    print(f"A razão entre os segmentos é {razao:.2f}.")
    print(f"Os segmentos formados pela bissetriz externa são {x:.2f} e {y:.2f}.")
