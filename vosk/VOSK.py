#!/usr/bin/env python
# coding: utf-8

# In[2]:


from vosk import Model, KaldiRecognizer
import pyaudio
import json
import pyttsx3
from Levenshtein import distance as lev


# In[3]:


model = Model("vosk-es")


# In[4]:


recognizer = KaldiRecognizer(model, 16000)
engine = pyttsx3.init()
engine.setProperty("rate", 120)
#engine.setProperty("voice", "spanish")
#engine.setProperty("volume", 1)

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
#rate = engine.getProperty("rate")
#engine.setProperty("rate", rate-50)


# In[5]:


voices = engine.getProperty("voices")
for p in voices:
    print(p)


# In[15]:


COMANDOS_MENU = {
    1:["contar cuento", "cuento", "quiero cuento"],
    2:["movimientos", "muevete", "activar movimientos"],
    3:["juego preguntas", "preguntas"]
}

COMANDOS_MOVIMIENTOS = {
    "parpadear":["parpadear", "cerrar los ojos", "parpadea"],
    "ojos":["virolo","mover los ojos", "ojos", "ojo"],
    "boca":["abre la boca", "boca"],
    "cabeza":["cabeza", "mueve la cabeza", "mueve cabeza", "cuello"]
}


#index_command = []

def f_wake_up():
    engine.say("Hola me llamo chocobot")
    engine.runAndWait()
    
def f_speak(text):
    engine.say(text)
    engine.runAndWait()
    
def f_recognize_command(COMANDOS, command):
    lev_speaken_command = []
    for k,v in COMANDOS.items():
        lev_menor = 100
        if command in v:
            return k
        else:
            lev_speaken_command.append(lev(command, v))           
            
            
            """print(lev(command, v), "\n", "--------------")
            
            for palabra in v:
                distancia = lev(command, v)
                print(distancia)
                if distancia < lev_menor:
                    lev_menor = distancia
            print("\n", "--------------")"""    
    
    index = lev_speaken_command.index(min(lev_speaken_command))
    return [list(COMANDOS.keys())[index],min(lev_speaken_command)]


# In[18]:


cap = pyaudio.PyAudio()
stream = cap.open(format=pyaudio.paInt16, 
#                  input_device_index=0,
                  channels=1, 
                  rate=16000,
                  input=True, 
                  frames_per_buffer=8192)
#                  output_device_index=0)
stream.start_stream()



while True:
    data = stream.read(4000, exception_on_overflow=False)
    if recognizer.AcceptWaveform(data):
        
        resultado = json.loads(recognizer.Result())
        print(resultado["text"])
        
        if "salir" in resultado["text"] or "terminar" in resultado["text"] or "chao" in resultado["text"]:
            f_speak("Hasta luego")
            break
        elif "hola" in resultado["text"]:
            f_wake_up()
        elif not resultado["text"]:
            pass
        else:
            respuesta_movimiento = f_recognize_command(COMANDOS_MOVIMIENTOS,resultado['text'])
            respuesta_menu = f_recognize_command(COMANDOS_MENU,resultado['text'])
            
            if (type(respuesta_movimiento) == list and type(respuesta_menu) == list):
                if respuesta_movimiento[1]<respuesta_menu[1]:
                    #hacer lo del menu: 1: cuento, 2: movimientos, 3: preguntas
                    if respuesta_menu[0] == 1:
                        f_speak("Vamos a comenzar con el cuento")
                    elif respuesta_menu[0] == 2:
                        f_speak("Dime que movimiento quieres que realice")
                    else:
                        f_speak("Empecemos con las preguntas")
                elif respuesta_movimiento[1]>respuesta_menu[1]:
                    f_speak("Voy a realizar el siguiente movimiento %" %respuesta_movimiento[0])
                else:
                    f_speak("No te escuche claramente, ¿podrias repetir tu peticion?")
            
            else:
                
                if type(respuesta_movimiento) == str:
                    f_speak("Voy a realizar el siguiente movimiento %s" %respuesta_movimiento)
                else:
                    if respuesta_menu == 1:
                        f_speak("Vamos a comenzar con el cuento")
                    elif respuesta_menu == 2:
                        f_speak("Dime que movimiento quieres que realice")
                    else:
                        f_speak("Empecemos con las preguntas")
                
                
                
            #print(respuesta)
            


# # Speech recognition library

# In[2]:


get_ipython().system('pip install speechrecognition')


# In[14]:


import speech_recognition as sr
r = sr.Recognizer()


# In[15]:


mic = sr.Microphone()
print(sr.Microphone.list_microphone_names())
mic = sr.Microphone(device_index=0)


# In[16]:


with mic as source:
    r.adjust_for_ambient_noise(source, duration=3)
    audio = r.listen(source)
    reconocimineto = r.recognize_google(audio, language="es-EC")
    print(reconocimineto)


# In[ ]:





# In[ ]:




