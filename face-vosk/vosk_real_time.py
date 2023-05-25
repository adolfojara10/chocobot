import vosk
import pyaudio
import json

global model, recognizer, p, stream

def f_start_model():
    global model, recognizer, p, stream

    model = vosk.Model("/home/catedra/Desktop/chocobot/chocobot/face-vosk/vosk-es")
    recognizer = vosk.KaldiRecognizer(model, 16000)

    

    #stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)

def f_speech_recognition():
    global model, recognizer, p, stream

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)

    empty_recognitions = 0
    is_answer = False
    print("------------habla-----------------")
    #stream.start_stream()
    respuesta = ""
    while True:
        data = stream.read(4096, exception_on_overflow=False)
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

            print(result['text'])
        
        if empty_recognitions == 1 and is_answer:
            break
    
    print("respuesta guardada\n" + respuesta)
    stream.stop_stream()
    stream.close()
    p.terminate()

    return respuesta


if __name__ == "__main__":
    f_start_model()
    f_speech_recognition()