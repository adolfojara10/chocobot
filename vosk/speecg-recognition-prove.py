import speech_recognition as sr
r = sr.Recognizer()

#mic = sr.Microphone(device_index=24)

mic = sr.Microphone()


for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
#print(sr.Microphone.list_microphone_names())
#mic = sr.Microphone(device_index=0)

print("Hablaaa--------")


with mic as source:
    r.adjust_for_ambient_noise(source, duration=3)
    audio = r.listen(source)
    reconocimineto = r.recognize_google(audio, language="en")
    print(reconocimineto)

