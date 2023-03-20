import pyttsx3

def f_say_text(text):
    engine = pyttsx3.init("espeak")
    engine.setProperty("voice", engine.getProperty("voices")[20].id)
    #engine.setProperty("voice", "english")
    engine.setProperty("volume", 1)
    engine.setProperty("rate", 150)

    engine.say(text)
    engine.runAndWait()

