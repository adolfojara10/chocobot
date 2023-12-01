import serial_reader
import face_recognition_functions
import threading
#import pygame
#pygame.init()
import cv2
import simon_dice
import movenet
import reproduce_sound
import subprocess
from pydub import AudioSegment
from pydub.playback import play
import os
import time
import sys
import serial
from playsound import playsound


global game_level_playing, video_capture

def f_reset_video_capture():
    global video_capture
    video_capture = cv2.VideoCapture(0, cv2.CAP_V4L2)
    video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
    video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)



if __name__ == "__main__":
    game_level_playing = ""
    
    # Define the command to list and kill processes using /dev/ttyTHS1
    command = 'lsof /dev/ttyTHS1 | awk \'NR>1 {print $2}\' | xargs -I {} kill -9 {}'

    # Execute the command using subprocess
    try:
        subprocess.run(command, shell=True, check=True)
        print("Processes using /dev/ttyTHS1 have been terminated.")
        sys.stdout.flush()
    except subprocess.CalledProcessError:
        print("Failed to terminate processes or no processes were found.")
        sys.stdout.flush()

    time.sleep(10)

    subprocess.run(["xhost", "+"], check=True)

    time.sleep(10)
    
    try:
        # Run the pulseaudio command as root
        result = subprocess.run(['sudo', 'pulseaudio', '-D', '--system'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        print(result.stdout)
        sys.stdout.flush()
    except subprocess.CalledProcessError as e:
        print(f"Error running pulseaudio: {e}")
        print(e.stdout)
        sys.stdout.flush()

    time.sleep(10)


    
    
            
    serial_reader.f_start_vars()
    simon_dice.f_reset_vars()
    face_recognition_functions.f_load_saved_faces()
    face_recognition_functions.f_reset_variables()
    movenet.f_load_model()
    movenet.f_reset_vars()
    #reproduce_sound.f_good("simon_dice_facil")
    #received_data = ""
    #received_data = "13 Adolfo Jara"
    #received_data = "conciencia_corporal_facil"
    """pygame.mixer.music.load("/home/catedra/Desktop/chocobot/chocobot/audios-estaticos/empezar_conversacion.mp3")

    # Play the audio file
    pygame.mixer.music.play()

    # Wait until playback is finished
    while pygame.mixer.music.get_busy():
        continue"""
    
    #path_to_audio = "/home/catedra/Desktop/chocobot/chocobot/audios-estaticos/empezar_conversacion.mp3"

    # Play the audio
    #playsound(path_to_audio)    

    # Create a thread for serial communication
    serial_thread = threading.Thread(target=serial_reader.serial_reader)

    # Start the serial communication thread
    serial_thread.start()

    """serial_port = "/dev/ttyACM0"
    baud_rate = 9600
    serial_connection = serial.Serial(serial_port, baud_rate)"""

    time.sleep(30)

    video_capture = cv2.VideoCapture(0, cv2.CAP_V4L2)
    video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
    video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)
    i = 0

    

    while True:
        ret, frame = video_capture.read()

        #print("camaraaaa")
        #sys.stdout.flush()

        if not ret:
            print("no sirve camara")
            sys.stdout.flush()
            f_reset_video_capture()

        else:

            if i == 0:
                print("cargando")
                sys.stdout.flush()
                face_recognition_functions.f_read_person_once(frame_received=frame)
                i+=1
                print("cargado")
                sys.stdout.flush()
                time.sleep(4)
                reproduce_sound.f_good("yoga_facil")

            """
            if " " in received_data:
                print("2")
                #crear persona

                face_recognition_functions.f_create_student(frame, received_data)

                if face_recognition_functions.is_user_saved == 1:
                    print("usuario guardado")
                    serial_reader.received_data = ""

                    serial_reader.f_send_data("1")

                    face_recognition_functions.f_reset_variables()
                elif face_recognition_functions.is_user_saved == -1:
                    serial_reader.f_send_data("-1")
                    print("usuario ya existe")"""
            
            """if "conciencia_corporal" in received_data:

                if movenet.interpreter is None:
                    movenet.f_load_model()
                    movenet.f_reset_vars()

                if received_data.split("_")[-1] == "facil":
                    #print("hhhhhh")
                    movenet.f_easy(frame)

                elif received_data.split("_")[-1] == "medio":
                    movenet.f_easy(frame)

                elif received_data.split("_")[-1] == "dificil":
                    movenet.f_easy(frame)"""

            
            
            if serial_reader.received_data == "leer_persona":
                print("1")
                sys.stdout.flush()

                face_recognition_functions.f_read_person(frame)
                #if face_recognition_functions.name_person != "Unknown" and face_recognition_functions.name_person != "":
                if face_recognition_functions.is_user_recognized == 1:
                    #reproduce_sound.f_welcome()
                    serial_reader.f_send_data(str(face_recognition_functions.id_person_recognized))
                    serial_reader.received_data = ""

                    face_recognition_functions.f_reset_variables()

                elif face_recognition_functions.is_user_recognized == -1:
                    print("No hay persona")
                    #reproduce_sound.f_no_user()
                    serial_reader.received_data = ""
                    face_recognition_functions.f_reset_variables()

                    serial_reader.f_send_data("-1")

                    # enviar que la persona no existe y crear el canvas en la tablet



            elif "jugar_robot" in serial_reader.received_data:
                cmd_send_arduino = serial_reader.received_data.split("_")[-1]
                # enviar datos al arduino

                # serial_connection.write(cmd_send_arduino.encode())

                
                game_level_playing = "jugar_robot"
                
                    
            elif " " in serial_reader.received_data and game_level_playing == "":
                print("2")
                sys.stdout.flush()
                #crear persona

                face_recognition_functions.f_create_student(frame, serial_reader.received_data)

                if face_recognition_functions.is_user_saved == 1:
                    print("usuario guardado")
                    sys.stdout.flush()
                    serial_reader.received_data = ""

                    serial_reader.f_send_data("1")

                    face_recognition_functions.f_reset_variables()
                    

                elif face_recognition_functions.is_user_saved == -1:
                    serial_reader.received_data = ""
                    serial_reader.f_send_data("-1")
                    print("usuario ya existe")
                    sys.stdout.flush()
                    
                    face_recognition_functions.f_reset_variables()
                    # reproducir sonido que el usuario ya existe

            elif "simon_dice" in serial_reader.received_data:
                game_level_playing = serial_reader.received_data
                
                if serial_reader.received_data.split("_")[-1] == "facil":
                    simon_dice.f_easy(frame)

                elif serial_reader.received_data.split("_")[-1] == "medio":
                    simon_dice.f_easy(frame)

                elif serial_reader.received_data.split("_")[-1] == "dificil":
                    simon_dice.f_easy(frame)
                
            elif "conciencia_corporal" in serial_reader.received_data:
                game_level_playing = serial_reader.received_data
                
                if serial_reader.received_data.split("_")[-1] == "facil":
                    movenet.f_easy(frame)

                elif serial_reader.received_data.split("_")[-1] == "medio":
                    movenet.f_easy(frame)

                elif serial_reader.received_data.split("_")[-1] == "dificil":
                    movenet.f_easy(frame)
                
            elif "yoga" in serial_reader.received_data:
                game_level_playing = serial_reader.received_data

                result = reproduce_sound.f_yoga(game_level_playing)

                serial_reader.f_send_data("game_completed")


                """
                if serial_reader.received_data.split("_")[-1] == "facil":
                    movenet.f_easy(frame)

                elif serial_reader.received_data.split("_")[-1] == "medio":
                    movenet.f_easy(frame)

                elif serial_reader.received_data.split("_")[-1] == "dificil":
                    movenet.f_easy(frame)
                """
            elif "good" in serial_reader.received_data:
                #reproducir reinforcement sound
                #reproduce_sound.f_good(serial_reader.received_data.split("_")[1])
                print(serial_reader.received_data)

                #random_number = random.randint(1, 3)
                #audio_dir = os.path.expanduser('/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/good/')
                #random_audio = str(random_number) + ".mp3"
                #audio_path = os.path.join(audio_dir, random_audio)
                #audio = AudioSegment.from_file(audio_path)
                #play(audio)
                
                #reproduce_sound.f_good("yoga_facil")

                reproduce_sound.f_good(game_level_playing)
                #print(game_level_playing)



                serial_reader.received_data = ""
                game_level_playing = ""




            elif "bad" in serial_reader.received_data:
                #reproducir reinforcement sound
                #reproduce_sound.f_good(serial_reader.received_data.split("_")[1])
                print(serial_reader.received_data)

                #random_number = random.randint(1, 3)
                #audio_dir = os.path.expanduser('/home/catedra/Desktop/chocobot/chocobot/face-bluetooth/audios/good/')
                #random_audio = str(random_number) + ".mp3"
                #audio_path = os.path.join(audio_dir, random_audio)
                #audio = AudioSegment.from_file(audio_path)
                #play(audio)

                reproduce_sound.f_bad()
                
                serial_reader.received_data = ""
                game_level_playing = ""



            elif "encuentra_diferencias" in serial_reader.received_data:
                game_level_playing = serial_reader.received_data

                #reproduce_sound.f_encuentra_diferencias()
                print(serial_reader.received_data)
                serial_reader.received_data = ""

            elif "completa_imagen" in serial_reader.received_data:
                game_level_playing = serial_reader.received_data

                #reproduce_sound.f_completa_imagen()
                print(serial_reader.received_data)
                serial_reader.received_data = ""

            elif "encuentra_objeto" in serial_reader.received_data:
                game_level_playing = serial_reader.received_data

                #reproduce_sound.f_encuentra_objeto()
                print(serial_reader.received_data)
                serial_reader.received_data = ""

            elif "atencion_auditiva" in serial_reader.received_data:
                game_level_playing = serial_reader.received_data

                #reproduce_sound.f_atencion_auditiva()
                print(serial_reader.received_data)
                serial_reader.received_data = ""

            elif "sonidos_naturaleza" in serial_reader.received_data:
                game_level_playing = serial_reader.received_data

                #reproduce_sound.f_sonidos_naturaleza()
                print(serial_reader.received_data)
                serial_reader.received_data = ""

            elif "jugar_robot" in serial_reader.received_data:
                game_level_playing = "jugar_robot"

            
            elif "cancelar" in serial_reader.received_data:
                game_level_playing = ""
                reproduce_sound.f_stop_sound()

            else:
                pass

            key = cv2.waitKey(1) & 0xFF

            # Hit 'q' on the keyboard to quit!
            if key == ord('q'):
                    # Release handle to the webcam
                video_capture.release()
                cv2.destroyAllWindows()
                #delete_files()
                #serial_thread.join()
                break

            #cv2.imshow('Video', frame)

        

