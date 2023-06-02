import vosk
import pyaudio
import json
import socket
import TTS
import serial
import subprocess
import numpy as np


global lista_despedida, model ,recognizer, p, stream, serial_connection

lista_despedida = ["chao ", "adios ", "adiós ", "hasta luego ", "nos vemos "]

def f_start_model():

    global model ,recognizer, p, stream, serial_connection

    model = vosk.Model("/home/catedra/Desktop/chocobot/chocobot/face-vosk/vosk-es")
    recognizer = vosk.KaldiRecognizer(model, 16000)

    serial_port = "/dev/ttyUSB0"
    baud_rate = 9600



    serial_connection = serial.Serial(serial_port, baud_rate)

    send_number_words_arduino(-2)

    # command = "sudo chmod a+rw /dev/ttyUSB0"

    # subprocess.call(command, shell=True)



def send_number_words_arduino(number_words):
    global serial_connection

    value_bytes = str(number_words).encode()

    serial_connection.write(value_bytes)  



def f_speech_recognition():

    global model ,recognizer, p, stream
    
    p = pyaudio.PyAudio()

    #host = "172.16.219.242"
    host = "192.168.117.209"
    port = 5005  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
   
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)


    empty_recognitions = 0
    is_answer = False

    #client_socket.send(message.encode())  # send message
    #data = client_socket.recv(1024).decode()
    print("------------habla-----------------")
    send_number_words_arduino(-1)
    respuesta = ""
    flag_loop = True
    while flag_loop:
        data = stream.read(4096, exception_on_overflow=False)
        if len(data) == 0:
            empty_recognitions += 1
            #print("1")
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            if result['text'] != "":
                is_answer = True
                
                respuesta += result["text"]
                respuesta += " "
                empty_recognitions = 0
                #print("2")
            else:
                empty_recognitions += 1
                #print("3")
            print(result['text'])
        
        if empty_recognitions == 1 and is_answer:
            print(respuesta)

            send_number_words_arduino(0)
            stream.stop_stream()
            if respuesta not in lista_despedida:
            #message = input(respuesta)  # take input
                client_socket.send(respuesta.encode())  # send message
                data_received = client_socket.recv(4096).decode()  # receive response



                send_number_words_arduino(np.ceil(len(data_received.split())/2))

                TTS.f_say_text(data_received)
                
                data = ""
                empty_recognitions = 0
                is_answer = False

                print('Received from server: ' + data_received)  # show in terminal

            else:

                TTS.f_say_text("Hasta luego. Espero verte pronto.")
                send_number_words_arduino(-2)
                flag_loop = False
                #client_socket.close()
                break
            
            stream.start_stream()
            respuesta = ""

    
    client_socket.close()  # close the connection
    print("Sesión terminada")
    stream.stop_stream()
    stream.close()
    p.terminate()

    return respuesta


if __name__ == "__main__":
    f_start_model()
    f_speech_recognition()