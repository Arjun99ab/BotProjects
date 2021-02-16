import pyttsx3
friend = pyttsx3.init()
voices = friend.getProperty('voices')
for voice in voices:
    print(voice, voice.id)
    friend.setProperty('voice', voice.id)
    friend.say("Hello World!")
    friend.runAndWait()
    friend.stop()
