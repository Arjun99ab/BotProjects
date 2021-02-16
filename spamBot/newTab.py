import pyautogui, time, keyboard
while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('|'):  # if key '5' is pressed
            print('You pressed a key!')
            pyautogui.hotkey('alt', 'tab')
            pyautogui.keyDown('ctrl')
            pyautogui.keyDown('t')
            pyautogui.keyUp('ctrl')
            pyautogui.keyUp('t')
            pyautogui.write('youtube.com')
            pyautogui.press('enter')
            pyautogui.moveTo(333, 459)
            time.sleep(6)
            pyautogui.click()
    except:
        print("still going")\

