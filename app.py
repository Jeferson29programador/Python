# NÃO ADIANTA PEGAR O CÓDIGO E QUERER RODAR SEM MUDAR AS COORDENAS!
# CADA JANELA TEM POSIÇÕES(COORDENADAS DIFERENTES)
# SENDO ASSIM, ASSISTA O VIDEO INTEIRO PARA ENTENDER COMO MONTAR ESTE PROGRAMA

import openpyxl
import pyperclip
import pyautogui
from time import sleep

# Entrar na planilha
workbook = openpyxl.load_workbook('produtos_ficticios.xlsx')
sheet_produtos = workbook['Produtos']
# Copiar informação de um campo e colar no seu campo correspondente
for linha in sheet_produtos.iter_rows(min_row=2):
    # Nome do Produto
    nome_produto = linha[0].value
    pyperclip.copy(nome_produto)
    pyautogui.click(1518,305,duration=1)
    pyautogui.hotkey('ctrl','v')

    # Descrição
    descricao = linha[1].value
    pyperclip.copy(descricao)
    pyautogui.click(1472,413,duration=1)
    pyautogui.hotkey('ctrl','v')
    
    # Categoria
    categoria = linha[2].value
    pyperclip.copy(categoria)
    pyautogui.click(1467,526,duration=1)
    pyautogui.hotkey('ctrl','v')

    # Codigo Produto
    codigo_produto = linha[3].value
    pyperclip.copy(codigo_produto)
    pyautogui.click(1481,614,duration=1)
    pyautogui.hotkey('ctrl','v')

    # Peso
    peso = linha[4].value
    pyperclip.copy(peso)
    pyautogui.click(1463,691,duration=1)
    pyautogui.hotkey('ctrl','v')

    # Dimensões
    dimensoes = linha[5].value
    pyperclip.copy(dimensoes)
    pyautogui.click(1465,783,duration=1)
    pyautogui.hotkey('ctrl','v')

    # Botão próximo
    pyautogui.click(1456,854,duration=1)
    sleep(3)

    # Preço
    preco = linha[6].value
    pyperclip.copy(preco)
    pyautogui.click(1539,325,duration=1)
    pyautogui.hotkey('ctrl','v')

    # Quantidade em estoque
    quantidade_em_estoque = linha[7].value
    pyperclip.copy(quantidade_em_estoque)
    pyautogui.click(1515,411,duration=1)
    pyautogui.hotkey('ctrl','v')

    # Data de validade
    data_de_validade = linha[8].value
    pyperclip.copy(data_de_validade)
    pyautogui.click(1504,501,duration=1)
    pyautogui.hotkey('ctrl','v')
    
    # Cor
    cor = linha[9].value
    pyperclip.copy(cor)
    pyautogui.click(1489,574,duration=1)
    pyautogui.hotkey('ctrl','v')

    # Tamanho
    tamanho = linha[10].value
    pyautogui.click(1530,670,duration=1)
    if tamanho == 'Pequeno':
        pyautogui.click(1520,705,duration=1)
    elif tamanho == 'Médio':
        pyautogui.click(1509,730,duration=1)
    else:
        pyautogui.click(1503,748,duration=1)

    # material    
    material = linha[11].value
    pyperclip.copy(material)
    pyautogui.click(1482,753,duration=1)
    pyautogui.hotkey('ctrl','v')
    # Botão próximo
    pyautogui.click(1494,808,duration=1)

    fabricante = linha[12].value
    pyperclip.copy(fabricante)
    pyautogui.click(1465,347,duration=1)
    pyautogui.hotkey('ctrl','v')

    pais_origem = linha[13].value
    pyperclip.copy(pais_origem)
    pyautogui.click(1473,426,duration=1)
    pyautogui.hotkey('ctrl','v')

    observacoes = linha[14].value
    pyperclip.copy(observacoes)
    pyautogui.click(1475,523,duration=1)
    pyautogui.hotkey('ctrl','v')

    codigo_de_barras = linha[15].value
    pyperclip.copy(codigo_de_barras)
    pyautogui.click(1471,655,duration=1)
    pyautogui.hotkey('ctrl','v')

    localizacao_armazem = linha[16].value
    pyperclip.copy(localizacao_armazem)
    pyautogui.click(1472,733,duration=1)
    pyautogui.hotkey('ctrl','v')

    # Botão concluir
    pyautogui.click(1485,814,duration=1)
    # Botão confirmar inclusão
    pyautogui.click(1887,198,duration=1)
    # Botão confirmação 2
    pyautogui.click(1886,191,duration=1)
    # iniciar cadastro novamente
    pyautogui.click(1695,580,duration=1)

# Repitir esses passos para outros campos até preencher campos daquela página
# Clicar em próxima
# Repetir os mesmos passos e ir para a próxima página(página 2)
# Repetir os mesmos passos e finalizar o cadastro daquele produto e clicar em concluir
# clicar em ok, para finalizar o processo
# Clicar no ok mais um vez na mensagem de confirmação de salvamento no banco de dados
# Clicar em "adicionar mais um e repetir o processo até finalizar a planilha"

