# Funções de verificação de semelhança

def verificar_lal(lado1_1, lado2_1, angulo_1, lado1_2, lado2_2, angulo_2):
    """Verifica se dois triângulos são semelhantes pelo critério LAL (Lado-Ângulo-Lado)."""
    return angulo_1 == angulo_2 and lado1_1 / lado1_2 == lado2_1 / lado2_2

def verificar_aa(angulo1_1, angulo2_1, angulo1_2, angulo2_2):
    """Verifica se dois triângulos são semelhantes pelo critério AA (Ângulo-Ângulo)."""
    return (angulo1_1 == angulo1_2 and angulo2_1 == angulo2_2) or (angulo1_1 == angulo2_2 and angulo2_1 == angulo1_2)

def verificar_lll(lado1_1, lado2_1, lado3_1, lado1_2, lado2_2, lado3_2):
    """Verifica se dois triângulos são semelhantes pelo critério LLL (Lado-Lado-Lado)."""
    return lado1_1 / lado1_2 == lado2_1 / lado2_2 == lado3_1 / lado3_2

# Função para obter dados do triângulo
def obter_triangulo(criterio):
    if criterio == "LAL":
        lado1 = float(input("Digite o primeiro lado: "))
        angulo = float(input("Digite o ângulo entre os lados: "))
        lado2 = float(input("Digite o segundo lado: "))
        return (lado1, angulo, lado2)

    elif criterio == "AA":
        angulo1 = float(input("Digite o primeiro ângulo: "))
        angulo2 = float(input("Digite o segundo ângulo: "))
        return (angulo1, angulo2)

    elif criterio == "LLL":
        lado1 = float(input("Digite o primeiro lado: "))
        lado2 = float(input("Digite o segundo lado: "))
        lado3 = float(input("Digite o terceiro lado: "))
        return (lado1, lado2, lado3)

# Função principal para verificar semelhança
def verificar_semelhanca(triangulo1, triangulo2, criterio):
    if criterio == "LAL":
        return verificar_lal(*triangulo1, *triangulo2)
    elif criterio == "AA":
        return verificar_aa(*triangulo1, *triangulo2)
    elif criterio == "LLL":
        return verificar_lll(*triangulo1, *triangulo2)
    else:
        print("Critério inválido.")
        return False

# Função para executar testes
def executar_testes():
    print("Iniciando testes...\n")
    
    # Teste LAL
    print("Teste LAL: lados (3, 4), ângulo 60 vs lados (6, 8), ângulo 60")
    assert verificar_lal(3, 4, 60, 6, 8, 60), "Erro no teste LAL!"
    
    # Teste AA
    print("Teste AA: ângulos (30, 60) vs ângulos (30, 60)")
    assert verificar_aa(30, 60, 30, 60), "Erro no teste AA!"
    
    # Teste LLL
    print("Teste LLL: lados (3, 4, 5) vs lados (6, 8, 10)")
    assert verificar_lll(3, 4, 5, 6, 8, 10), "Erro no teste LLL!"
    
    print("Todos os testes passaram com sucesso!")

# Programa principal
criterio = input("Escolha o critério de semelhança (LAL, AA, LLL): ").upper()

print("Digite os valores para o primeiro triângulo:")
triangulo1 = obter_triangulo(criterio)

print("Digite os valores para o segundo triângulo:")
triangulo2 = obter_triangulo(criterio)

resultado = verificar_semelhanca(triangulo1, triangulo2, criterio)

if resultado:
    print(f"Os triângulos são semelhantes pelo critério {criterio}.")
else:
    print(f"Os triângulos não são semelhantes pelo critério {criterio}.")






