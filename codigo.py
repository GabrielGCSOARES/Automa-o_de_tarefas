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

# Passo 3; Importar a base de dados
# Passo 4: fazer o cadastro do produtos sendo seu código,marca, tipo,categoria, preço,custo,OBS
# Passo 5: Repetir para todos os produtos 

#pyautogui -> fazer automações com pyhton
