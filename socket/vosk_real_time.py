import vosk
import pyaudio
import json
import socket

global lista_despedida

lista_despedida = ["chao", "adios", "adiós", "hasta luego", "nos vemos"]

def f_speech_recognition():
    model = vosk.Model("/home/catedra/Desktop/chocobot/chocobot/face-vosk/vosk-es")
    recognizer = vosk.KaldiRecognizer(model, 16000)

    host = "172.16.212.34"
    port = 1234  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)

    empty_recognitions = 0
    is_answer = False

    #client_socket.send(message.encode())  # send message
    #data = client_socket.recv(1024).decode()
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
            print(respuesta)
            #message = input(respuesta)  # take input
            client_socket.send(respuesta.encode())  # send message
            data = client_socket.recv(1024).decode()  # receive response

            respuesta = ""
            is_answer = False

            print('Received from server: ' + data)  # show in terminal

            if respuesta in lista_despedida:
                break

    
    client_socket.close()  # close the connection
    print("respuesta guardada")
    stream.stop_stream()
    stream.close()
    p.terminate()

    return respuesta


if __name__ == "__main__":
    f_speech_recognition()