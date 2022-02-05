from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import time


login = open('Login.txt', 'r')
usernameesenha = login.readlines()
number = 1
number2 = 3
linhas = (usernameesenha[number])
linhas2 = (usernameesenha[number2])
limit = 100
print('==================================================')
time.sleep(1.4)
print('IIII  NNNNN    NNN   SSSSSSSS  TTTTTTTT   AAAAA')
print('IIII  NNN NN   NNN   SSS         TTT    AAA    AAA')
print('IIII  NNN  NN  NNN   SSSSSSSS    TTT    AAAAAAAAAA')
print('IIII  NNN   NN NNN        SSS    TTT    AAA    AAA')
print('IIII  NNN    NNNNN   SSSSSSSS    TTT    AAA    AAA')
print('                                                  ')
print('                                                  ')
time.sleep(1.4)
print('  AAAAA     UUU   UUU  TTTTTTTTT   OOOOOOOOOO')
print('AAA   AAA   UUU   UUU     TTT      OOO    OOO')
print('AAAAAAAAA   UUU   UUU     TTT      OOO    OOO')
print('AAA   AAA   UUU   UUU     TTT      OOO    OOO')
print('AAA   AAA   UUUUUUUUU     TTT      OOOOOOOOOO')
print('                                                  ')
print('                                                  ')
time.sleep(1.4)
print('SSSSSSSS   UUU   UUU   BBBBBBBB    SSSSSSSS')
print('SSS        UUU   UUU   BBB    BBB  SSS')
print('SSSSSSSS   UUU   UUU   BBB   BB    SSSSSSSS')
print('     SSS   UUU   UUU   BBB    BBB       SSS')
print('SSSSSSSS   UUUUUUUUU   BBBBBBBB    SSSSSSSS')
print('==================================================')
time.sleep(1.4)
print('visit my github:https://github.com/PauloVitorBots')
time.sleep(1.4)
language = input('whats your language ?/Qual seu idioma ? eng=english por=português\n')

if language == ('eng'):
    print('if you dont know how to use it, go to:\n\nand search README.md')
    time.sleep(1.4)
    url = input('enter the url of the post you want to like.\n')
    account = int(input('tell how many accounts you put in the txt file(max 100).\n'))
    time.sleep(0.7)
    print('the process will start, just maximize the window and dont click anything else.')
    navegador = webdriver.Chrome()

if language == ('por'):
    print('se você não sabe como usar esse script, vá para:\n\ne procure o arquivo README.md')
    time.sleep(1.4)
    url = input('coloque a url da publicação que deseja curtir.\n')
    account = int(input('diga quantas contas você colocou no arquivo txt(maximo 100).\n'))
    time.sleep(0.7)
    print('o processo vai começar, apenas maximize a janela e não clique nada mais.')
    navegador = webdriver.Chrome()

for limit in range(account):
    number = number + 4
    number2 = number2 + 4
    linhas = (usernameesenha[number])
    linhas2 = (usernameesenha[number2])
    navegador.get('https://www.instagram.com/')
    username = linhas
    senha = linhas2
    time.sleep(3)
    navegador.find_element(By.XPATH, "//input[@name='username']").click()
    time.sleep(1.2)
    pyautogui.hotkey('f','backspace','backspace','backspace')
    time.sleep(0.5)
    pyautogui.write(username)
    time.sleep(1.2)
    navegador.find_element(By.XPATH, "//input[@name='password']").click()
    time.sleep(0.5)
    pyautogui.hotkey('f','backspace','backspace','backspace')
    time.sleep(1.2)
    pyautogui.write(senha)
    time.sleep(1)
    pyautogui.press('Enter')
    time.sleep(1.2)
    navegador.get(url)
    time.sleep(3)
    pyautogui.click(x=835, y=507)
    time.sleep(1.2)
    navegador.get('https://www.instagram.com/')
    time.sleep(1.5)
    pyautogui.click(x=687, y=567)
    time.sleep(1.5)
    pyautogui.click(x=1131, y=149)
    time.sleep(0.8)
    pyautogui.click(x=1056, y=346)
    time.sleep(0.8)
