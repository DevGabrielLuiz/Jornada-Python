import pyautogui as gui
import time 

# Passo 1 - entrar no sistema da empresa
    # Abrir o link
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
gui.PAUSE = 1
gui.press('win')# permite pressionar uma tecla 
gui.write('chrome')# permite digitar no teclado
gui.press('enter')
gui.write(link)
gui.press('enter')
# time.sleep(3)
gui.press('tab')


# gui.click()# permite clicar na tela
# gui.scroll()# permite scrolar a tela
# # gui.hotkey() combinação de teclas
# gui.click(x=663, y=337)# permite clicar na tela


# 2 - Fazer login
# se houver um autopreenchimento no campos eu posso utilizar a tecla hotkey 
#  gui.hotkey('ctrl','a')
gui.write('Gabriel@.com')
gui.press('tab')
gui.write()
gui.press('tab')
gui.press('enter')

# 3 Importar a base de dados ou tabela 
import pandas as pd
base_dados = pd.read_csv('produtos.csv')
# 4 - Cadastrar produtos
for linha in base_dados.index:   # index é como o python chama as linhas 
    
    # codigo
    gui.press('tab')
    codigo = str(base_dados.loc[linha,'codigo'])# 'loc' vem de localizar
    gui.write(codigo)
    # marca 
    gui.press('tab')
    marca = str(base_dados.loc[linha,'marca'])
    gui.write(marca)
    # tipo
    gui.press('tab')
    tipo = str(base_dados.loc[linha,'tipo'])
    gui.write(tipo)
    # categoria 
    gui.press('tab')
    categoria = str(base_dados.loc[linha,'categoria'])
    gui.write(categoria)
    # preço_unitario
    gui.press('tab')
    preco = str(base_dados.loc[linha,'preco_unitario'])
    gui.write(preco)
    # custo
    gui.press('tab')
    custo = str(base_dados.loc[linha,'custo'])
    gui.write(custo)
    # obs
    gui.press('tab')
    obs = str(base_dados.loc[linha,'obs'])
    if obs != 'nan':    
        gui.write(obs)
    # enviar
    gui.press('tab')
    gui.press('enter')
    # voltar pro topo
    gui.scroll(1000) or gui.press('pgup')
# 5 - Repetir o passo 4 até cadastrar todos os produtos