import math

# Função fornecida pela questão
def funcao_exercicio_4(x):
    # Retorna o valor da função y = 1 - x * ln(x)
    return 1 - x * math.log(x)

# Implementação do Método da Bisseção
def metodo_bissecao(f, a, b, precisao):
    # Verifica se o método da Bisseção pode ser aplicado no intervalo fornecido
    if f(a) * f(b) >= 0:
        print("O método da Bisseção não pode ser aplicado. O intervalo fornecido não contém uma mudança de sinal.")
        return None
    
    # Inicializa o contador de iterações
    iteracoes = 0
    
    # Executa o loop até que a precisão desejada seja alcançada
    while (b - a) / 2 > precisao:
        iteracoes += 1  # Incrementa o número de iterações
        c = (a + b) / 2  # Calcula o ponto médio do intervalo
        
        # Verifica se o ponto médio é a raiz exata
        if f(c) == 0:
            return c, iteracoes  # Retorna a raiz encontrada e o número de iterações
        
        # Verifica em qual subintervalo a raiz está localizada
        elif f(a) * f(c) < 0:
            b = c  # Atualiza o limite superior do intervalo
        else:
            a = c  # Atualiza o limite inferior do intervalo

    # Retorna a raiz aproximada e o número de iterações
    return (a + b) / 2, iteracoes

# Definindo o intervalo e a precisão
intervalo_a = 1.5
intervalo_b = 2.0
precisao = 0.01

# Executando o Método da Bisseção para encontrar a raiz
raiz, numero_iteracoes = metodo_bissecao(funcao_exercicio_4, intervalo_a, intervalo_b, precisao)

# Exibindo o resultado da raiz aproximada e o número de iterações necessárias
print(f"Raiz aproximada: {raiz}")
print(f"Número de iterações: {numero_iteracoes}")
