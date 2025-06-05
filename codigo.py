import pyautogui 
import time 


pyautogui.PAUSE = 1


# Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# espera 3 segundos
time.sleep(3)

# Passo 2: Fazer o login
pyautogui.click(x=649, y=477)
pyautogui.write("malenia@email.com")
time.sleep(0.5)
pyautogui.press("tab")
pyautogui.write("minhasasd")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)
# Passo 3; Importar a base de dados
import pandas 

#esse tabela é uma variavel 
tabela = pandas.read_csv("produtos.csv")
print(tabela)


# Passo 4: cadastrar o 1 produto
pyautogui.click(x=613, y=328)

codigo = "MOLO000251"
pyautogui.write(codigo)

marca = "Logitech"
pyautogui.press("tab")
pyautogui.write(marca)

tipo = " Mouse"
pyautogui.press("tab")
pyautogui.write(tipo)

categoria = "1"
pyautogui.press("tab")
pyautogui.write(categoria)

preco_unitario = "25.95"
pyautogui.press("tab")
pyautogui.write(preco_unitario)

custo = "6.5"
pyautogui.press("tab")
pyautogui.write(custo)

obs = ""
pyautogui.press("tab")
pyautogui.write(obs)

pyautogui.press("tab")#passou para o botão enviar
pyautogui.press("enter")

pyautogui.scroll(10000)
# Passo 5: Repetir para todos os produtos 

#pyautogui -> fazer automações com pyhton
