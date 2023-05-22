import vosk
import pyaudio
import json

def f_speech_recognition():
    model = vosk.Model("vosk-es")
    recognizer = vosk.KaldiRecognizer(model, 16000)

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)

    empty_recognitions = 0
    is_answer = False
    print("------------habla-----------------")
    respuesta = ""
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if len(data) == 0:
            empty_recognitions += 1
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            if result['text'] != "":
                is_answer = True
                respuesta += result["text"]
                empty_recognitions = 0
            else:
                empty_recognitions += 1
            #print(result['text'])
        
        if empty_recognitions == 2 and is_answer:
            break
    
    print("respuesta guardada")
    stream.stop_stream()
    stream.close()
    p.terminate()

    return respuesta

