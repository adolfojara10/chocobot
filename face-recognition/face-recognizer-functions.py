import face_recognition
import cv2
import numpy as np
import pandas as pd

# global variables 
global known_face_encodings
global known_face_names 
global face_locations
global face_encodings
global face_names
global frame
global rgb_small_frame

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
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        # # If a match was found in known_face_encodings, just use the first one.
        # if True in matches:
        #     first_match_index = matches.index(True)
        #     name = known_face_names[first_match_index]

        # Or instead, use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        print(face_distances)
        try:
            best_match_index = np.argmin(face_distances)
            print(best_match_index, "----------------------", matches, "--------------")#, matches[best_match_index])
            

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
    print(new_face_array)

    known_face_encodings.append(new_face_encoding)
    #face_encodings.append(str(len(known_face_names)))
    print("aqui face: ", "\n", new_face_encoding.tolist())
    known_face_names.append(str(len(known_face_names)+1))

    new_data = pd.DataFrame(new_face_array)
    new_data["Nombre"] = str(len(known_face_names)+1)
    #print(new_data)

    all_data = pd.read_csv("./data/caras.csv")
    all_data.append(new_data, ignore_index=True)
    print(all_data)
    all_data.to_csv("./data/caras.csv", index = False, mode='a')




def f_start():
    f_reset_variables()

    f_load_saved_faces()

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

        if face_locations != []:
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            f_recognize_names()
            
        else:
            face_encodings = []

        f_draw_faces()

        key = cv2.waitKey(1) & 0xFF

        # Hit 'q' on the keyboard to quit!
        if key == ord('q'):
            break
        elif key == ord('s'): # and not "Unknown" in face_names:
            #nombre = input("Escribe tu nombre")
            print("guardando nombre")
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)[0]
            f_save_name(face_encodings)


        # Display the resulting image
        cv2.imshow('Video', frame)


if __name__ == "__main__":
    f_start()