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
pandas.read_csv("produtos.csv")


# Passo 4: fazer o cadastro do produtos sendo seu código,marca, tipo,categoria, preço,custo,OBS
# Passo 5: Repetir para todos os produtos 

#pyautogui -> fazer automações com pyhton
