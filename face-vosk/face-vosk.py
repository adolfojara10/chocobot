import cv2
import face_recognition
#import pygame
#pygame.init()
from pydub import AudioSegment
from pydub.playback import play
import numpy as np
import pandas as pd
import os
# import TTS
# import threading
import vosk_real_time
import tkinter2
import time
import vosk_socket
# import subprocess

from gtts import gTTS

# global variables 
global known_face_encodings
global known_face_names 
global known_face_ids
global face_locations
global face_encodings
global new_face_encodings
global face_names
global frame
global rgb_small_frame
global name_person
global list_check_person
global window_new_face
global answer_create_user


def f_reset_variables():
    global face_locations
    global face_encodings
    global face_names
    global name_person
    global list_check_person
    global window_new_face
    global answer_create_user

    face_locations = []
    face_encodings = []
    face_names = []
    name_person = ""
    list_check_person = []
    window_new_face = False
    answer_create_user = "no"

    

# function to load saved faces
def f_load_saved_faces():
    data = pd.read_csv("/home/catedra/Desktop/chocobot/chocobot/face-vosk/data/caras.csv")
    #print(data)

    global known_face_names    
    known_face_names = data["Nombre"].tolist()

    global known_face_encodings
    known_face_encodings = data.iloc[:,0:-2].values.tolist()

    global known_face_ids
    known_face_ids = data["ID"].tolist()

    #print(known_face_encodings.values.tolist())


def f_recognize_names():
    global face_names
    global face_encodings
    global new_face_encodings
    global known_face_names
    global known_face_encodings
    global name_person
    global list_check_person
    global window_new_face
    global answer_create_user

    face_names = []
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.5)
        name = "Unknown"

        # # If a match was found in known_face_encodings, just use the first one.
        # if True in matches:
        #     first_match_index = matches.index(True)
        #     name = known_face_names[first_match_index]

        # Or instead, use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        #print(face_distances)
        try:
            best_match_index = np.argmin(face_distances)
            #print(best_match_index, "----------------------", matches, "--------------")#, matches[best_match_index])
            


            #recognizes the name of the person
            if matches[best_match_index]: #and best_match_index > 0.6:
                name = known_face_names[best_match_index].split()[0]
                list_check_person.append(1)

                #greet the person


                if name_person == "" and name != "Unknown" and list_check_person.count(1)==17:
                    name_person = name
                    # thread1 = threading.Thread(target= f_say_hi)
                    # thread1.start()

                    f_say_hi()

                    audio = AudioSegment.from_file("/home/catedra/Desktop/chocobot/chocobot/audios-estaticos/empezar_conversacion.mp3")
                    vosk_socket.send_number_words_arduino(2)

                    play(audio)

                    """
                    pygame.mixer.music.load("/home/catedra/Desktop/chocobot/chocobot/audios-estaticos/empezar_conversacion.mp3")

                    vosk_socket.send_number_words_arduino(2)

                    # Play the audio file
                    pygame.mixer.music.play()

                    # Wait until playback is finished
                    while pygame.mixer.music.get_busy():
                        continue"""

                    """
                    # Construct the command to play the audio file
                    play_command = f"aplay /home/catedra/Desktop/chocobot/chocobot/audios/empezar_conversacion.wav"

                    # Execute the command to play the audio file
                    subprocess.run(play_command, shell=True)"""

                    #TTS.f_say_text("¿Quieres comenzar una conversación?")



                    vosk_socket.send_number_words_arduino(-1)


                    answer_conversation = vosk_real_time.f_speech_recognition()

                    vosk_socket.send_number_words_arduino(0)

                    print(answer_conversation)

                    if answer_conversation == "si" or answer_conversation == "sí":
                        vosk_socket.f_speech_recognition()
                        print("Conexion con servidor exitosa")
                        time.sleep(2)
                        #TTS.f_say_text("Empecemos")

                    name_person = ""



            #should call to save the new person and ask the name
            elif name_person == "" and list_check_person.count(0)==20 and answer_create_user=="no":
                list_check_person = []
                # thread2 = threading.Thread(target= TTS.f_say_text("¿Deseas guardar tu nombre?"))
                # thread2.start()
                #answer = input("Save name?")

                #TTS.f_say_text("¿Deseas guardar tu nombre?")

                # Construct the command to play the audio file

                audio = AudioSegment.from_file("/home/catedra/Desktop/chocobot/chocobot/audios-estaticos/guardar_nombre.mp3")
                vosk_socket.send_number_words_arduino(2)
                play(audio)

                """
                pygame.mixer.music.load("/home/catedra/Desktop/chocobot/chocobot/audios-estaticos/guardar_nombre.mp3")

                vosk_socket.send_number_words_arduino(2)
                # Play the audio file
                pygame.mixer.music.play()

                # Wait until playback is finished
                while pygame.mixer.music.get_busy():
                    continue"""

                """
                play_command = f"aplay /home/catedra/Desktop/chocobot/chocobot/audios/guardar_nombre.wav"

                # Execute the command to play the audio file
                subprocess.run(play_command, shell=True)"""

                vosk_socket.send_number_words_arduino(-1)

                #descomentar esta linea para que funcione con vosk
                
                answer_create_user = vosk_real_time.f_speech_recognition().lower()


                vosk_socket.send_number_words_arduino(0)



                list_check_person = []
                #if answer_create_user == "si" and window_new_face==False and tkinter2.run_thread == False:
                if answer_create_user == "si" or answer_create_user == "sí":

                    print("abrir ventana")
                    new_face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations, num_jitters=5, model="large")[0]
                    #f_save_name_id(face_encodings)
                    window_new_face = True
                    #thread4 =threading.Thread(target=f_call_window_new_face)
                    #thread4.start()

                    f_call_window_new_face()
                    answer_create_user = "no"

                    if tkinter2.value1 != "" and tkinter2.value2 != "" and tkinter2.save_name:
                        f_save_name_id()

                    print(tkinter2.run_thread)

                    
                else:
                    pass
                

                

            elif name == "Unknown":
                list_check_person.append(0)
                #print(len(list_check_person))

            if len(list_check_person)==50:
                list_check_person = []
                



        except ValueError:
            pass
        face_names.append(name)


def f_draw_faces():
    global frame 
    global face_names
    global face_locations

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        #print(face_locations)

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, str(name), (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)


def f_save_name(new_face_encoding):

    global known_face_encodings
    global known_face_names
    

    #new_face = new_face_encoding.tolist()
    #new_face.append(str(len(known_face_names)+1))
    #print("new face: \n", new_face)
    new_face_array = np.array(new_face_encoding)
    new_face_array = new_face_array.reshape(1,-1)
    #print(new_face_array)

    known_face_encodings.append(new_face_array.flatten().tolist())
    #face_encodings.append(str(len(known_face_names)))
    #print("aqui face: ", "\n", new_face_encoding.tolist())
    known_face_names.append(str(len(known_face_names)+1))

    new_data = pd.DataFrame(new_face_array)
    new_data["Nombre"] = str(len(known_face_names))
    #print("nuevos: \n",new_data)

    try:

        #print(known_face_encodings)
        da = pd.DataFrame(known_face_encodings)
        #nombre = input("¿Cual es tu nombre?")
        
        da["Nombre"] = known_face_names

        #print("otra forma: \n", da)

        da.to_csv("/home/catedra/Desktop/chocobot/chocobot/face-vosk/data/caras.csv", index = False)

        print("usuario guardado")

        """all_data = pd.read_csv("./data/caras.csv")
        print("antiguo \n",all_data)

        df3 = pd.concat([all_data, new_data], ignore_index = False)
        df3.reset_index()
        print("unidos \n", df3)

        os.remove("./data/caras.csv")        

        df3 = all_data.append(new_data, ignore_index=False)
        #print(all_data["Nombre"])
        df3.to_csv("./data/caras.csv", index = False, mode='w')#, header=False)"""
    except:
        print("exception")
        new_data.to_csv("/home/catedra/Desktop/chocobot/chocobot/face-vosk/data/caras.csv", index = False)#, header=False)


def f_prove_existance(prove_face_encoding):
    global known_face_encodings

    matches = face_recognition.compare_faces(known_face_encodings, prove_face_encoding)

    if True in matches:
        return True
    else:
        return False


def f_start():

    vosk_real_time.f_start_model()
    vosk_socket.f_start_model()

    f_reset_variables()

    try:
        f_load_saved_faces()
    except:
        global known_face_encodings
        global known_face_names
        
        known_face_names = []

        known_face_encodings = []

    """global known_face_encodings
    global known_face_names
    
    known_face_names = []vosk_socket.send_number_words_arduino(1)

    known_face_encodings = []"""

    global face_locations
    global face_encodings
    global face_names
    global window_new_face
    global name_person
    global list_check_person
    
    video_capture = cv2.VideoCapture(0)


    while True:
        
        global frame
        global rgb_small_frame

        ret, frame = video_capture.read()

        frame = cv2.flip(frame, 1)

        #if process_this_frame:
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]
        
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame, model="cnn", number_of_times_to_upsample=2)

        #print(face_locations)

        if face_locations != []:
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations, num_jitters=3, model="large")
            #print(-*25, "face encodings: ", len(face_encodings), -*25)
            if len(face_encodings) == 1:
                f_recognize_names()
                f_draw_faces()
            else:
                audio = AudioSegment.from_file("/home/catedra/Desktop/chocobot/chocobot/audios-estaticos/2_personas.mp3")
                vosk_socket.send_number_words_arduino(4)
                vosk_socket.send_number_words_arduino(0)
                play(audio)

            
        else:
            face_encodings = []
            list_check_person.append(-1)

            if list_check_person.count(-1)==30:
                name_person = ""

            


        #f_draw_faces()

        key = cv2.waitKey(1) & 0xFF

        # Hit 'q' on the keyboard to quit!
        if key == ord('q'):
                # Release handle to the webcam
            video_capture.release()
            cv2.destroyAllWindows()
            delete_files()
            break

        """
        elif key == ord('s'): # and not "Unknown" in face_names:
            #nombre = input("Escribe tu nombre")
            print("guardando nombre")

            
            #face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations, num_jitters=5, model="large")[0]
            
            if "Unknown" in face_names:

                index = face_names.index("Unknown")

                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations[index], num_jitters=5, model="large")[0]               

            #elif not f_prove_existance(face_encodings):
           
             #   f_save_name(face_encodings)
            else:
                print("Persona ya existe")"""


        # Display the resulting image
        cv2.imshow('Video', frame)


#function to say hi or to ask for the name
def f_say_hi():
    global name_person

    text = "Hola, " + str(name_person)

    print(text)

    tts = gTTS(text=text, lang='es-us')

    directory = '/home/catedra/Desktop/chocobot/chocobot/audios/'
    file_count = len(os.listdir(directory))

    # Generate the output file name
    output_file = os.path.join(directory, f'welcome_{file_count}.mp3')

    
    # Save the audio file
    tts.save(output_file)

    audio = AudioSegment.from_file(output_file)
    play(audio)

    """

    pygame.init()

    # Load the audio file
    pygame.mixer.music.load(output_file)

    vosk_socket.send_number_words_arduino(2)

    # Play the audio file
    pygame.mixer.music.play()

    # Wait until playback is finished
    while pygame.mixer.music.get_busy():
        continue

    pygame.quit()"""


    #TTS.f_say_text(data_received)

"""
    directory = '/home/catedra/Desktop/chocobot/chocobot/audios/'
    file_count = len(os.listdir(directory))

    # Generate the output file name
    output_file = os.path.join(directory, f'welcome_{file_count}.wav')

                
    # Construct the command to generate the audio file
    generate_command = f"echo '{text}' | /home/catedra/piper/piper/piper --model /home/catedra/piper/es-mls_9972-low.onnx --output_file {output_file}"

    # Execute the command to generate the audio file
    subprocess.run(generate_command, shell=True)

    time.sleep(2)
    # Construct the command to play the audio file
    play_command = f"aplay {output_file}"

    # Execute the command to play the audio file
    subprocess.run(play_command, shell=True)"""


def f_save_name_id():

    # thread3 = threading.Thread(target= TTS.f_say_text("¿Cómo te llamas?"))
    # thread3.start()
    # thread3.join()
    

    global known_face_encodings
    global known_face_names
    global known_face_ids
    global new_face_encodings

    #new_name = vosk_real_time.f_speech_recognition().capitalize()

    nombres, apellidos = tkinter2.return_name_values()
    new_name = nombres + " " + apellidos
    new_name = new_name.capitalize()

    new_face_array = np.array(new_face_encodings)
    new_face_array = new_face_array.reshape(1,-1)
    print(new_face_array)


    known_face_encodings.append(new_face_array.flatten().tolist())
    known_face_ids.append(str(len(known_face_names)+1))
    known_face_names.append(new_name)
    
    #known_face_names.append(str(len(known_face_names)+1))

    new_data = pd.DataFrame(new_face_array)
    new_data["ID"] = str(len(known_face_names))
    new_data["Nombre"] = new_name

    try:

        #print(known_face_encodings)
        da = pd.DataFrame(known_face_encodings)
        #nombre = input("¿Cual es tu nombre?")
        da["ID"] = known_face_ids
        da["Nombre"] = known_face_names

        #print("otra forma: \n", da)

        print(da)

        da.to_csv("/home/catedra/Desktop/chocobot/chocobot/face-vosk/data/caras.csv", index = False)

        print("usuario guardado")

        """all_data = pd.read_csv("./data/caras.csv")
        print("antiguo \n",all_data)

        df3 = pd.concat([all_data, new_data], ignore_index = False)
        df3.reset_index()
        print("unidos \n", df3)

        os.remove("./data/caras.csv")        

        df3 = all_data.append(new_data, ignore_index=False)
        #print(all_data["Nombre"])
        df3.to_csv("./data/caras.csv", index = False, mode='w')#, header=False)"""
    except:
        print("exception---------------------")
        new_data.to_csv("./data/caras.csv", index = False)#, header=False)


def f_call_window_new_face():

    global known_face_names
    if window_new_face:
        tkinter2.start()


    """
    global known_face_names
    thread3 = threading.Thread(target=tkinter2.start())
    #starts the thread
    if window_new_face:
        thread3.start()

    #closes the thread
    elif window_new_face==False and thread3.isAlive():

        print("cerrar ventana")
        tkinter2.change_state_thread(False)
        thread3.join()
        nombres, apellidos = tkinter2.save_inputs()
        new_name = nombres + " " + apellidos
        new_name = new_name.capitalize()

        if not new_name in known_face_names:
            f_save_name_id()
            """


def delete_files():

    #delete all the audio files created in the session
    directory = "/home/catedra/Desktop/chocobot/chocobot/audios/"
    
    # Get a list of all files in the directory
    file_list = os.listdir(directory)

    # Iterate over the files and delete them
    for file_name in file_list:
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Deleted file: {file_path}")


if __name__ == "__main__":
    f_start()

