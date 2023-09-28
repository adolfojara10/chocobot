import serial_reader
import face_recognition_functions
import threading
import cv2
import simon_dice

#global received_data


if __name__ == "__main__":
    serial_reader.f_start_vars()
    simon_dice.f_reset_vars()
    face_recognition_functions.f_load_saved_faces()
    face_recognition_functions.f_reset_variables()
    
    #received_data = ""
    received_data = "13 Adolfo Jara"


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

        
        
        if serial_reader.received_data == "leer_persona":
            print("1")
            face_recognition_functions.f_read_person(frame)
            #if face_recognition_functions.name_person != "Unknown" and face_recognition_functions.name_person != "":
            if face_recognition_functions.is_user_recognized == 1:
                #arreglar para que sea el id de la persona
                serial_reader.f_send_data("2")
                serial_reader.received_data = ""

                # enviar el id a la tablet

                face_recognition_functions.f_reset_variables()

            elif face_recognition_functions.is_user_recognized == -1:
                print("No hay persona")
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

        

