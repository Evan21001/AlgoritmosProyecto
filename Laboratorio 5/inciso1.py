import pyautogui
localizar_imagen= pyautogui.localOnScreen('lab5.jpg')
centro_de_la_imagen = pyautogui.center(localizar_imagen)
pyautogui.doubleClick(centro_de_la_imagen)
tiem.sleep(5)
pyautogui.typewrite('Hello world!\n', interval=secs_between_keys)




