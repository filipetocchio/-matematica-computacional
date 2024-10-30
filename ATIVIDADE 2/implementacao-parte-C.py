def verifica_interseccao_bissetriz_externa(lado1, lado2):
    return "A bissetriz externa NÃO intercepta o prolongamento do lado oposto" if lado1 == lado2 else "A bissetriz externa INTERCEPTA o prolongamento do lado oposto"

# Exemplo de uso:
lado1 = float(input("Digite o comprimento de um lado adjacente: "))
lado2 = float(input("Digite o comprimento do outro lado adjacente: "))

print(verifica_interseccao_bissetriz_externa(lado1, lado2))
