import cv2
from tkinter import N
from unittest import result
import face_recognition


import pandas as pd
import numpy as np
import os
import serial

# global variables 
global known_face_encodings
global known_face_names 
global face_locations
global face_encodings
global face_names
global frame
global rgb_small_frame
global arduino_communication



def f_reset_variables():
    global face_locations
    global face_encodings
    global face_names

    face_locations = []
    face_encodings = []
    face_names = []

# function to load saved faces
def f_load_saved_faces():
    data = pd.read_csv("./data/caras.csv")

    global known_face_names    
    known_face_names = data["Nombre"].tolist()

    global known_face_encodings
    known_face_encodings = data.iloc[:,0:-1].values.tolist()

    #print(known_face_encodings.values.tolist())


def f_recognize_names():
    global face_names
    global face_encodings
    global known_face_names
    global known_face_encodings

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
            

            if matches[best_match_index]: #and best_match_index > 0.6:
                name = known_face_names[best_match_index]
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

        #print(top, right, bottom, left)

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        #center_face_x = (right-left)
        #center_face_y = (bottom-top)

        """center_face_x = int(((right-left)/2)+left)
        center_face_y = int(((bottom-top)/2)+top)
        print(center_face_x, center_face_y)
        cv2.circle(frame, (center_face_x, center_face_y), 4, (0,255,255), cv2.FILLED)"""

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, str(name), (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        f_follow_person()


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


def f_start():
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
    
    known_face_names = []

    known_face_encodings = []"""

    global face_locations
    global face_encodings
    global face_names
    
    video_capture = cv2.VideoCapture(0)

    i=0

    while True:
        
        global frame
        global rgb_small_frame

        ret, frame = video_capture.read()

        frame = cv2.flip(frame, 1)

        frame_clahe = f_automatic_brightness_and_contrast()

        #if process_this_frame:
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]
        
        # Find all the faces in the current frame of video
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

        elif key == ord('s'): # and not "Unknown" in face_names:sudo pip3 install -U jetson-stats
            #nombre = input("Escribe tu nombre")
            print("guardando nombre")

            
            #face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations, num_jitters=5, model="large")[0]
            
            if "Unknown" in face_names:

                index = face_names.index("Unknown")

                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations[index], num_jitters=5, model="large")[0]               

            #elif not f_prove_existance(face_encodings):
           
             #   f_save_name(face_encodings)
            else:
                print("Persona ya existe")

        if i==1:

            result = cv2.absdiff(cv2.cvtColor(frame_clahe, cv2.COLOR_BGR2GRAY), cv2.cvtColor(frame_clahe2, cv2.COLOR_BGR2GRAY))
            _, result = cv2.threshold(result, 20, 255, cv2.THRESH_BINARY)
            cv2.imshow("Movimiento", result)

        frame_clahe2 = frame_clahe

        i=1

        # Display the resulting image
        cv2.imshow('Video', frame)
        cv2.imshow("Preprocesamiento", frame_clahe)


def f_connect_arduino():
    global arduino_communication

    arduino_communication = serial.Serial("/dev/ttyUSB0",9600, write_timeout=10)
    print("conexion exitosa")


def f_follow_person():
    global face_locations
    global frame
    global arduino_communication

    for (top, right, bottom, left) in face_locations:
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # frame shape
        height, width, _ = frame.shape

        #extract center of the face
        center_face_x = int(((right-left)/2)+left)
        center_face_y = int(((bottom-top)/2)+top)
        #print(center_face_x, center_face_y)
        cv2.circle(frame, (center_face_x, center_face_y), 4, (0,255,255), cv2.FILLED)

        #center of frame
        center_frame = int(width/2)

        

        if center_face_x < center_frame - 50:
            #left movement
            print("izquierda")
            arduino_communication.write("i".encode())
        elif center_face_x > center_frame + 50:
            arduino_communication.write("d".encode())
        elif center_face_x == center_frame:
            arduino_communication.write("p".encode())




# Automatic brightness and contrast optimization with optional histogram clipping
def f_automatic_brightness_and_contrast(clip_hist_percent=25):
    global frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calculate grayscale histogram
    hist = cv2.calcHist([gray],[0],None,[256],[0,256])
    hist_size = len(hist)

    # Calculate cumulative distribution from the histogram
    accumulator = []
    accumulator.append(float(hist[0]))
    for index in range(1, hist_size):
        accumulator.append(accumulator[index -1] + float(hist[index]))

    # Locate points to clip
    maximum = accumulator[-1]
    clip_hist_percent *= (maximum/100.0)
    clip_hist_percent /= 2.0

    # Locate left cut
    minimum_gray = 0
    while accumulator[minimum_gray] < clip_hist_percent:
        minimum_gray += 1

    # Locate right cut
    maximum_gray = hist_size -1
    while accumulator[maximum_gray] >= (maximum - clip_hist_percent):
        maximum_gray -= 1

    # Calculate alpha and beta values
    alpha = 255 / (maximum_gray - minimum_gray)
    beta = -minimum_gray * alpha

    '''
    # Calculate new histogram with desired range and show histogram 
    new_hist = cv2.calcHist([gray],[0],None,[256],[minimum_gray,maximum_gray])
    plt.plot(hist)
    plt.plot(new_hist)
    plt.xlim([0,256])
    plt.show()
    '''

    auto_result = cv2.convertScaleAbs(frame, alpha=alpha, beta=beta)
    return auto_result


if __name__ == "__main__":
    
    f_connect_arduino()

    f_start()

