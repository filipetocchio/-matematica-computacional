# Explicação da Lógica do Algoritmo

## 1. Entrada de Dados dos Triângulos

O algoritmo inicia solicitando ao usuário as medidas de dois triângulos, incluindo lados e ângulos. As entradas de dados são ajustadas conforme o critério selecionado para verificar a semelhança (LAL, AA ou LLL).

- **Critério LAL:** Solicita dois lados e o ângulo entre eles.
- **Critério AA:** Solicita dois ângulos.
- **Critério LLL:** Requer todos os três lados.

## 2. Critérios de Semelhança

- **Critério LAL (Lado-Ângulo-Lado):**
  - A semelhança é confirmada quando os ângulos entre os lados correspondentes dos dois triângulos são congruentes e os lados ao redor desse ângulo mantêm uma relação de proporção constante.
  - **Exemplo:** Para triângulos com lados (lado1_1, lado2_1) e ângulo angulo_1 em comparação a (lado1_2, lado2_2) e angulo_2, verificamos a igualdade dos ângulos e a proporcionalidade entre lado1_1/lado1_2 == lado2_1/lado2_2.

- **Critério AA (Ângulo-Ângulo):**
  - A semelhança ocorre quando dois ângulos dos triângulos são congruentes, garantindo que o terceiro ângulo também será congruente.
  - A congruência dos dois ângulos confirma que os triângulos são semelhantes por este critério, sem necessidade de verificar os lados.

- **Critério LLL (Lado-Lado-Lado):**
  - A semelhança é verificada quando todos os lados dos dois triângulos possuem uma relação de proporção constante entre si.
  - Para os lados (lado1_1, lado2_1, lado3_1) de um triângulo e (lado1_2, lado2_2, lado3_2) do outro, os três devem satisfazer lado1_1/lado1_2 == lado2_1/lado2_2 == lado3_1/lado3_2.

## 3. Verificação de Semelhança

Após coletar os dados dos triângulos, a função principal de verificação identifica o critério e chama a função correspondente (verificar_lal, verificar_aa ou verificar_lll). Cada função retorna True ou False, dependendo se a condição de semelhança é satisfeita.

## 4. Resultado Final

Se um critério de semelhança é validado, uma mensagem indicando o critério específico é exibida, afirmando que os triângulos são semelhantes. Caso contrário, o algoritmo informa que os triângulos não são semelhantes.

