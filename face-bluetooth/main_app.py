from serial_reader import serial_reader
import face_recognition_functions
import threading
import cv2

global received_data


if __name__ == "__main__":
    face_recognition_functions.f_load_saved_faces()
    face_recognition_functions.f_reset_variables()
    
    received_data = "leer_persona"


    # Create a thread for serial communication
    #serial_thread = threading.Thread(target=serial_reader)

    # Start the serial communication thread
    #serial_thread.start()

    video_capture = cv2.VideoCapture(0, cv2.CAP_V4L2)
    video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
    video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

    

    while True:
        ret, frame = video_capture.read()

        if not ret:
            print("no sirve")
            break
        

        if received_data == "leer_persona":
            print("1")
            face_recognition_functions.f_read_person(frame)
            if face_recognition_functions.name_person != "Unknown" and face_recognition_functions.name_person != "":
                received_data = ""
                # enviar el id a la tablet



                
        elif " " in received_data:
            #crear persona
            pass
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

        

