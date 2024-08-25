salario = float(input("Digite o salário do funcionário: R$"))

# Verifica se o salário é superior a R$1.250,00 e calcula o aumento correspondente
if salario > 1250.00:
    aumento = salario * 0.10  # 10% de aumento para salários superiores a R$1.250,00
else:
    aumento = salario * 0.15  # 15% de aumento para salários inferiores ou iguais a R$1.250,00

# Calcula o novo salário, somando o aumento ao salário original


# Exibe o valor do aumento e o novo salário
print(f"O aumento salarial é de R${salario}.")
print(f"O novo salário é de R${salario}.")