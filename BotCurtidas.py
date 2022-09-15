import webbrowser
import pyautogui
from time import sleep

'''
Bom dia, Boa tarde, Boa noite, me chamo Caique Sena e sou Analista QA - Junior
Hoje desenvolvi um bot que automatiza o processo de dar curtidas em qualquer postagem no instagram, neste teste que estou trazendo a voces, ele vai ir na página da nike, clicar na primeira postagem, e verificar se ela tem curtida, se ela nao estiver curtida, ela irá detectar e fazer o processo para curtir uma publicação

Lembrando que consigo automatizar qualquer processo manual e transforma-lo em um bot que lhe poupara bastante tempo! Isto é apenas um exemplo
'''

pyautogui.alert('Iremos começar')

webbrowser.open('https://www.instagram.com/sena.xw7/')
pyautogui.sleep(3)

pyautogui.moveTo(603,101)

pyautogui.mouseDown()
pyautogui.mouseUp()

pyautogui.write('nike')
pyautogui.sleep(3)

pyautogui.moveTo(564,160)
pyautogui.click()
pyautogui.sleep(5)

pyautogui.scroll(-500)


#Clicando na primeira foto da nike
pyautogui.moveTo(348,360)
pyautogui.click()
pyautogui.sleep(3)

coracao = pyautogui.locateCenterOnScreen('coracao.png')
sleep(1)

if coracao is not None:
    sleep(86400)
elif coracao == None:
    pyautogui.click(675,567,duration=1)
    sleep(5)