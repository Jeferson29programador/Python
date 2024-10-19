def calcular_erros(valor_exato, valor_aproximado):
    # Calcula o erro absoluto, relativo e percentual
    erro_absoluto = abs(valor_exato - valor_aproximado)  # Diferença absoluta entre os valores
    erro_relativo = erro_absoluto / abs(valor_exato)  # Razão entre o erro absoluto e o valor exato
    erro_percentual = erro_relativo * 100  # Converte o erro relativo para percentual
    return erro_absoluto, erro_relativo, erro_percentual

# Casos fornecidos pelo exercício
caso_1_exato = 0.00005
caso_1_aproximado = 0.00004

caso_2_exato = 101000
caso_2_aproximado = 100000

# Calculando os erros para o Caso 1
erro_absoluto_1, erro_relativo_1, erro_percentual_1 = calcular_erros(caso_1_exato, caso_1_aproximado)

# Calculando os erros para o Caso 2
erro_absoluto_2, erro_relativo_2, erro_percentual_2 = calcular_erros(caso_2_exato, caso_2_aproximado)

# Exibindo os resultados para o Caso 1
print(f"Erro Absoluto Caso 1: {erro_absoluto_1}")
print(f"Erro Relativo Caso 1: {erro_relativo_1}")
print(f"Erro Percentual Caso 1: {erro_percentual_1}%\n")

# Exibindo os resultados para o Caso 2
print(f"Erro Absoluto Caso 2: {erro_absoluto_2}")
print(f"Erro Relativo Caso 2: {erro_relativo_2}")
print(f"Erro Percentual Caso 2: {erro_percentual_2}%\n")

# Comparando a precisão entre os dois casos
if erro_relativo_1 < erro_relativo_2:
    print("A aproximação do Caso 1 é mais precisa.")
elif erro_relativo_1 > erro_relativo_2:
    print("A aproximação do Caso 2 é mais precisa.")
else:
    print("As aproximações dos dois casos têm a mesma precisão.")
