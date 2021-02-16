import pyautogui, time, keyboard, webbrowser

play = True

zoom = False

while play:
    try:
        if keyboard.is_pressed('f'):
            print('Time for FTC')

            url= 'https://us04web.zoom.us/j/77818493208?pwd=bHhEdDUzcjFoOW0xUUlZaUpnQitsUT09'

            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

            zoom = True

        elif keyboard.is_pressed('d'):
            print('Time for Debate')

            url = 'https://us02web.zoom.us/j/87323617084'

            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

            zoom = True

        elif keyboard.is_pressed('m'):
            print('Time for Math Team')

            url = 'https://mcpsmd.zoom.us/w/85702152484?tk=LxbeRB_qIhvUMDT_ejd8Y4drIAMl48458e4e2lsORKI.DQIAAAAT9D8RJBZZREhhRU1QLVFlcTZ4RWktODBkVm93AAAAAAAAAAAAAAAAAAAAAAAAAAAA&pwd=V2dnS3dxd3pGOXlBMUZXeVRvVktiQT09'

            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

            zoom = True

        if zoom == True:
            webbrowser.get(chrome_path).open(url)

            time.sleep(5)

            pyautogui.press('left')
            pyautogui.press('enter')

            time.sleep(4)

            pyautogui.press('enter')

            play = False

    except:
        print("running")
