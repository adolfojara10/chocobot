from vosk import Model, KaldiRecognizer
import pyaudio
import json

model = Model("/home/catedra/Desktop/chocobot/chocobot/face-vosk/vosk-es")
recognizer = KaldiRecognizer(model, 16000)


cap = pyaudio.PyAudio()
stream = cap.open(format=pyaudio.paInt16, 
#                  input_device_index=0,
                  channels=1, 
                  rate=16000,
                  input=True, 
                  frames_per_buffer=8192)
#                  output_device_index=0)
stream.start_stream()

print("Habla: --------------")
while True:
    data = stream.read(4000, exception_on_overflow=False)
    if recognizer.AcceptWaveform(data):
        
        resultado = json.loads(recognizer.Result())
        print(resultado["text"])

