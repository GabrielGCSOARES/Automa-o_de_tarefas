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
for linha in tabela.index: 

    pyautogui.click(x=613, y=328)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)

    marca = tabela.loc[linha, "marca"]
    pyautogui.press("tab")
    pyautogui.write(marca)

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.press("tab")
    pyautogui.write(tipo)

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.press("tab")
    pyautogui.write(categoria)

    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.press("tab")
    pyautogui.write(preco_unitario)

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.press("tab")
    pyautogui.write(custo)

    obs = str(tabela.loc[linha, "obs"])
    pyautogui.press("tab")
    
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")#passou para o botão enviar
    pyautogui.press("enter")

    pyautogui.scroll(10000)




#pyautogui -> fazer automações com pyhton
