import json
import socket
import pyaudio
import os
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

global lista_despedida, model ,recognizer, p, stream, serial_connection

lista_despedida = ["chao ", "adios ", "adiós ", "hasta luego ", "nos vemos "]


def f_chat():
    global model, recognizer, p, stream

    p = pyaudio.PyAudio()

    host = "192.168.253.209"
    port = 5005  # socket server port number

    client_socket = socket.socket()  # instantiate
    try:
        client_socket.connect((host, port))  # connect to the server
        print("Connected to server")

        while True:
            message = input("Enter a message to send to the server (or 'exit' to quit): ")
            if message.lower() == 'exit':
                break
            else:
                client_socket.send(message.encode())  # send message
                data_received = client_socket.recv(4096).decode()  # receive response

                print("respuesta: \n ", data_received)

                tts = gTTS(text=data_received, lang='es-us')

                directory = '/home/catedra/Desktop/chocobot/chocobot/audios/'
                file_count = len(os.listdir(directory))

                # Generate the output file name
                output_file = os.path.join(directory, f'welcome_{file_count}.mp3')

               
                # Save the audio file
                tts.save(output_file)

                audio = AudioSegment.from_file(output_file)
                play(audio)

                # Rest of your code to process the received data

        print("Connection closed")
        client_socket.close()

    except ConnectionRefusedError:
        print("Connection to the server failed. Make sure the server is running.")

if __name__ == "__main__":
    f_chat()
