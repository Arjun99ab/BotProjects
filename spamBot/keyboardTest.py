import keyboard, pyautogui
while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('5'):  # if key '5' is pressed
            print('You pressed a key!')
            break  # finishing the loop5
    except:
        break  # if user pressed a key other than the given key the loop will break
