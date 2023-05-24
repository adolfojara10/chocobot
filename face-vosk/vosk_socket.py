import vosk
import pyaudio
import json
import socket

global lista_despedida, model ,recognizer, p, stream

lista_despedida = ["chao", "adios", "adiós", "hasta luego", "nos vemos"]

def f_start_model():

    global model ,recognizer, p, stream

    model = vosk.Model("/home/catedra/Desktop/chocobot/chocobot/face-vosk/vosk-es")
    recognizer = vosk.KaldiRecognizer(model, 16000)

    p = pyaudio.PyAudio()

    




def f_speech_recognition():

    global model ,recognizer, p, stream

    #host = "172.16.219.242"
    host = "192.168.205.209"
    port = 5005  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
   
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=8192)


    empty_recognitions = 0
    is_answer = False

    #client_socket.send(message.encode())  # send message
    #data = client_socket.recv(1024).decode()
    print("------------habla-----------------")
    respuesta = ""
    flag_loop = True
    while flag_loop:
        data = stream.read(4000, exception_on_overflow=False)
        if len(data) == 0:
            empty_recognitions += 1
            #print("1")
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            if result['text'] != "":
                is_answer = True
                respuesta += result["text"]
                empty_recognitions = 0
                #print("2")
            else:
                empty_recognitions += 1
                #print("3")
            #print(result['text'])
        
        if empty_recognitions == 1 and is_answer:
            print(respuesta)
            stream.stop_stream()
            #message = input(respuesta)  # take input
            client_socket.send(respuesta.encode())  # send message
            data_received = client_socket.recv(4096).decode()  # receive response

            
            data = ""
            empty_recognitions = 0
            is_answer = False

            print('Received from server: ' + data_received)  # show in terminal

            if respuesta in lista_despedida:
                flag_loop = False
                #client_socket.close()
                break
            
            stream.start_stream()
            respuesta = ""

    
    client_socket.close()  # close the connection
    print("respuesta guardada")
    stream.stop_stream()
    stream.close()
    p.terminate()

    return respuesta


if __name__ == "__main__":
    f_speech_recognition()