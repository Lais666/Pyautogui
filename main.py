import time
import pyautogui
import pandas

pyautogui.PAUSE = 0.5
#Abrir o navegador
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.click(x=415, y=921)
pyautogui.click(x=1508, y=97)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(3)
# Acessar o site do sistema com login e senha
pyautogui.click(x=552, y=564)
pyautogui.write('lais.sinatra@gmail.com')
pyautogui.press('tab')
pyautogui.write('senha')
pyautogui.click(x=961, y=797)

# Inserir todas as informações do produto
tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Enviar as informações para o sistema
# Repetir o cadastro até acabar o cadastro de todos os produtos
for linha in tabela.index:
    pyautogui.click(x=599, y=388)
    pyautogui.write(str(tabela.loc[linha, 'codigo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')
    observacao = str(tabela.loc[linha, 'obs'])
    if observacao != 'nan':
        pyautogui.write(observacao)
    pyautogui.click(x=825, y=811)
    pyautogui.scroll(5000)
