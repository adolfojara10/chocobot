import serial_reader
import face_recognition_functions
import threading
import cv2
import simon_dice
import movenet
import reproduce_sound
import subprocess

#global received_data


if __name__ == "__main__":
    # Define the command to list and kill processes using /dev/ttyTHS1
    command = 'lsof /dev/ttyTHS1 | awk \'NR>1 {print $2}\' | xargs -I {} kill -9 {}'

    # Execute the command using subprocess
    try:
        subprocess.run(command, shell=True, check=True)
        print("Processes using /dev/ttyTHS1 have been terminated.")
    except subprocess.CalledProcessError:
        print("Failed to terminate processes or no processes were found.")

        
    serial_reader.f_start_vars()
    simon_dice.f_reset_vars()
    face_recognition_functions.f_load_saved_faces()
    face_recognition_functions.f_reset_variables()
    movenet.f_load_model()
    movenet.f_reset_vars()
    
    #received_data = ""
    #received_data = "13 Adolfo Jara"
    #received_data = "conciencia_corporal_facil"


    # Create a thread for serial communication
    serial_thread = threading.Thread(target=serial_reader.serial_reader)

    # Start the serial communication thread
    serial_thread.start()

    video_capture = cv2.VideoCapture(0, cv2.CAP_V4L2)
    video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
    video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

    

    while True:
        ret, frame = video_capture.read()

        if not ret:
            print("no sirve camara")
            break

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




                
        elif " " in serial_reader.received_data:
            print("2")
            #crear persona

            face_recognition_functions.f_create_student(frame, serial_reader.received_data)

            if face_recognition_functions.is_user_saved == 1:
                print("usuario guardado")
                serial_reader.received_data = ""

                serial_reader.f_send_data("1")

                face_recognition_functions.f_reset_variables()
                

            elif face_recognition_functions.is_user_saved == -1:
                serial_reader.received_data = ""
                serial_reader.f_send_data("-1")
                print("usuario ya existe")
                
                face_recognition_functions.f_reset_variables()
                # reproducir sonido que el usuario ya existe

        elif "simon_dice" in serial_reader.received_data:

            if serial_reader.received_data.split("_")[-1] == "facil":
                simon_dice.f_easy(frame)

            elif serial_reader.received_data.split("_")[-1] == "medio":
                simon_dice.f_easy(frame)

            elif serial_reader.received_data.split("_")[-1] == "dificil":
                simon_dice.f_easy(frame)

        elif "conciencia_corporal" in serial_reader.received_data:

            if serial_reader.received_data.split("_")[-1] == "facil":
                movenet.f_easy(frame)

            elif serial_reader.received_data.split("_")[-1] == "medio":
                movenet.f_easy(frame)

            elif serial_reader.received_data.split("_")[-1] == "dificil":
                movenet.f_easy(frame)

        elif "yoga" in serial_reader.received_data:

            if serial_reader.received_data.split("_")[-1] == "facil":
                movenet.f_easy(frame)

            elif serial_reader.received_data.split("_")[-1] == "medio":
                movenet.f_easy(frame)

            elif serial_reader.received_data.split("_")[-1] == "dificil":
                movenet.f_easy(frame)

        elif "good" in serial_reader.received_data:
            #reproducir reinforcement sound
            #reproduce_sound.f_good(serial_reader.received_data.split("_")[1])
            print(serial_reader.received_data)
            serial_reader.received_data = ""

        elif "bad" in serial_reader.received_data:
            #reproducir reinforcement sound
            #reproduce_sound.f_bad(serial_reader.received_data.split("_")[1])
            print(serial_reader.received_data)
            serial_reader.received_data = ""

        elif "encuentra_diferencias" in serial_reader.received_data:
            #reproduce_sound.f_encuentra_diferencias()
            print(serial_reader.received_data)
            serial_reader.received_data = ""

        elif "completa_imagen" in serial_reader.received_data:
            #reproduce_sound.f_completa_imagen()
            print(serial_reader.received_data)
            serial_reader.received_data = ""

        elif "encuentra_objeto" in serial_reader.received_data:
            #reproduce_sound.f_encuentra_objeto()
            print(serial_reader.received_data)
            serial_reader.received_data = ""

        elif "atencion_auditiva" in serial_reader.received_data:
            #reproduce_sound.f_atencion_auditiva()
            print(serial_reader.received_data)
            serial_reader.received_data = ""

        elif "sonidos_naturaleza" in serial_reader.received_data:
            #reproduce_sound.f_sonidos_naturaleza()
            print(serial_reader.received_data)
            serial_reader.received_data = ""

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

        cv2.imshow('Video', frame)

        

