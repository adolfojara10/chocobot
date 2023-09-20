import cv2
import face_recognition

import numpy as np
import pandas as pd
#import os

# global variables 
global known_face_encodings
global known_face_names 
global known_face_ids
global face_locations
global face_encodings
global face_names
global frame
global rgb_small_frame
global name_person
global list_check_person

def f_reset_variables():
    global face_locations
    global face_encodings
    global face_names
    global name_person
    global list_check_person

    face_locations = []
    face_encodings = []
    face_names = []
    name_person = ""
    list_check_person = []



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

    #print(known_face_encodings)


def f_recognize_names():
    global face_names
    global face_encodings
    global known_face_names
    global known_face_encodings
    global name_person
    global list_check_person


    face_names = []
    #print(face_encodings)
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

                print(list_check_person, name, name_person)


                if name_person == "" and name != "Unknown" and list_check_person.count(1)==17:
                    name_person = name
                    print("persona reconocida")
                    # thread1 = threading.Thread(target= f_say_hi)
                    # thread1.start()
                    """
                    f_say_hi()

                    audio = AudioSegment.from_file("/home/catedra/Desktop/chocobot/chocobot/audios-estaticos/empezar_conversacion.mp3")
                    vosk_socket.send_number_words_arduino(2)

                    play(audio)

                    """



            #should call to save the new person and ask the name
            elif name_person == "" and list_check_person.count(0)==20:
                list_check_person = []
                print("no hay persona")
                # thread2 = threading.Thread(target= TTS.f_say_text("¿Deseas guardar tu nombre?"))
                # thread2.start()
                #answer = input("Save name?")

                #TTS.f_say_text("¿Deseas guardar tu nombre?")

                # Construct the command to play the audio file
                """
                audio = AudioSegment.from_file("/home/catedra/Desktop/chocobot/chocobot/audios-estaticos/guardar_nombre.mp3")
                vosk_socket.send_number_words_arduino(2)
                play(audio)

                """
                

                

            elif name == "Unknown":
                list_check_person.append(0)
                #print(len(list_check_person))

            if len(list_check_person)==50:
                list_check_person = []
                



        except ValueError:
            print("error")
            pass

        face_names.append(name)
        #print("+++++++++++++++++++++++\n", face_names)


def f_draw_faces():
    global frame 
    global face_names
    global face_locations

    #print("draw faces")
    #print(face_locations)
    #print("-----------------------------------\n", face_names)

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        print("draw faces 2")
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
        da["Nombre"] = known_face_names

        #print("otra forma: \n", da)

        da.to_csv("./data/caras.csv", index = False)

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
        new_data.to_csv("./data/caras.csv", index = False)#, header=False)


def f_prove_existance(prove_face_encoding):
    global known_face_encodings

    matches = face_recognition.compare_faces(known_face_encodings, prove_face_encoding)

    if True in matches:
        return True
    else:
        return False


def f_read_person(frame_received):
    global frame, rgb_small_frame, face_locations, name_person, list_check_person, face_encodings

    frame = frame_received

    frame = cv2.flip(frame, 1)

    #if process_this_frame:
    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]
    
    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_small_frame, model="cnn", number_of_times_to_upsample=2)

    if face_locations != []:
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations, num_jitters=3, model="large")
        #print(-*25, "face encodings: ", len(face_encodings), -*25)
        #print("face location != [] len face encodings: ", len(face_encodings))
        if len(face_encodings) == 1:
            #print("in")
            #f_draw_faces()
            f_recognize_names()
            
        else:
            print("2+ personas")
            """
            audio = AudioSegment.from_file("/home/catedra/Desktop/chocobot/chocobot/audios-estaticos/2_personas.mp3")
            vosk_socket.send_number_words_arduino(4)
            vosk_socket.send_number_words_arduino(0)
            play(audio)"""

        
    else:

        face_encodings = []
        list_check_person.append(-1)

        if list_check_person.count(-1)==30:
            name_person = ""

        


    




def f_start():
    #print("hola")
    f_reset_variables()

    try:
        f_load_saved_faces()
    except Exception as e:

        print(e)
        global known_face_encodings
        global known_face_names
        
        known_face_names = []

        known_face_encodings = []
    #print("hola")
    """global known_face_encodings
    global known_face_names
    
    known_face_names = []

    known_face_encodings = []"""

    global face_locations
    global face_encodings
    global face_names
    
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
            f_recognize_names()
            
        else:
            face_encodings = []

        f_draw_faces()

        key = cv2.waitKey(1) & 0xFF

        # Hit 'q' on the keyboard to quit!
        if key == ord('q'):
                # Release handle to the webcam
            video_capture.release()
            cv2.destroyAllWindows()
            break


        # Display the resulting image
        cv2.imshow('Video', frame)



