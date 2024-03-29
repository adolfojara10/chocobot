import cv2
import tensorflow as tf
import numpy as np
import time
from serial_reader import f_send_data
import reproduce_sound

global EDGES
global step, is_command_sounded, left_foot, right_foot, i_clap, is_game_finished, right_hand,interpreter, frame
interpreter = None

EDGES = {
    (0, 1): 'm',
    (0, 2): 'c',
    (1, 3): 'm',
    (2, 4): 'c',
    (0, 5): 'm',
    (0, 6): 'c',
    (5, 7): 'm',
    (7, 9): 'm',
    (6, 8): 'c',
    (8, 10): 'c',
    (5, 6): 'y',
    (5, 11): 'm',
    (6, 12): 'c',
    (11, 12): 'y',
    (11, 13): 'm',
    (13, 15): 'm',
    (12, 14): 'c',
    (14, 16): 'c'
}

def f_reset_vars():
    global step, is_command_sounded, left_foot, right_foot, i_clap, is_game_finished, right_hand, interpreter

    i_clap = 0
    step = 0
    is_command_sounded = False
    left_foot = None
    right_hand = None
    is_game_finished = False


def f_load_model():
    global interpreter
    
    interpreter = tf.lite.Interpreter(model_path='lite-model_movenet_singlepose_lightning_3.tflite')
    interpreter.allocate_tensors()


def f_read(frame_received):
    
    global EDGES, interpreter

    if frame_received is None:
        # Handle the case where frame_received is None
        print("Received a None frame.")
    else:
            

        #img = tf.image.resize_with_pad(np.expand_dims(frame_received, axis=0), 256,256)
        img = tf.image.resize_with_pad(np.expand_dims(frame_received, axis=0), 192,192)
        input_image = tf.cast(img, dtype=tf.float32)
        
        # Setup input and output 
        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()
        
        # Make predictions 
        interpreter.set_tensor(input_details[0]['index'], np.array(input_image))
        interpreter.invoke()
        keypoints_with_scores = interpreter.get_tensor(output_details[0]['index'])

        y, x, c = frame_received.shape
        shaped = np.squeeze(np.multiply(keypoints_with_scores, [y,x,1]))

        return shaped


def f_easy(frame_received, confidence_threshold=0.1):
    global step, is_command_sounded, left_foot, right_foot, i_clap, is_game_finished
    #two_d_array = np.array(keypoints).reshape(-1, keypoints.shape[-1])
    #step = 3
    y, x, c = frame_received.shape
    keypoints_with_scores = f_read(frame_received)

    keypoints = np.squeeze(np.multiply(keypoints_with_scores, [y,x,1]))
    #draw_connections(keypoints_with_scores, EDGES, 0.4)
    #draw_keypoints(keypoints_with_scores, 0.4)
    
    print(str(step))

    if step == 0:
        if not is_command_sounded:
            #reproducir sonido
            #reproduce_sound.f_movenet()
            reproduce_sound.f_easy_movenet(step+1)
            is_command_sounded = True

        print("0")

        if (keypoints[9][0] < keypoints[0][0] and keypoints[10][0] < keypoints[0][0] and keypoints[9][2] > confidence_threshold and keypoints[0][2] > confidence_threshold and keypoints[10][2] > confidence_threshold):
            print("yessss")
            step+=1
            is_command_sounded = False

    elif step == 1:
        
        print("1")
        if not is_command_sounded:
            #reproducir sonido
            reproduce_sound.f_easy_movenet(step+1)
            is_command_sounded = True

        if ((abs(keypoints[9][0] - keypoints[8][0]) < 20 or abs(keypoints[9][1] - keypoints[8][1]) < 20 or abs(keypoints[7][0] - keypoints[9][0]) < 20) and (keypoints[9][2] >= confidence_threshold or keypoints[8][2] > confidence_threshold or keypoints[7][2] > confidence_threshold)) or ((abs(keypoints[10][0] - keypoints[7][0]) < 20 or abs(keypoints[10][1] - keypoints[7][1]) < 20 or abs(keypoints[10][0] - keypoints[8][0]) < 20) and (keypoints[10][2] >= confidence_threshold or keypoints[7][2] >= confidence_threshold or keypoints[8][2] >= confidence_threshold)):
            print("yesss2222")
            step+=1
            is_command_sounded = False

    elif step == 2:
        
        if not is_command_sounded:
            #reproducir sonido
            reproduce_sound.f_easy_movenet(step+1)
            print("hola")
            time.sleep(3)
            left_foot = None
            is_command_sounded = True
            #left_foot = keypoints[15]
            #right_foot = keypoints[16]
        
        try:
            if left_foot == None:
                if keypoints[15][2] > confidence_threshold+0.2 and keypoints[16][2] > confidence_threshold:
                    left_foot = keypoints[15]
                    right_foot = keypoints[16]
        except:
            #print()
            pass
        

        try:
            #print(left_foot[0] - keypoints[15][0], "    ---------------------------      ", right_foot[0] - keypoints[16][0])
            #print(left_foot[0], " --------- ", keypoints[15][0], "    --------------      ", right_foot[0], " ---------------- ", keypoints[16][0], " ++++++++ ", keypoints[15][2], " ++++ ", keypoints[16][2])
            if (abs(left_foot[0] - keypoints[15][0]) > 30 or right_foot[0] - keypoints[16][0] > 30) and (keypoints[15][2] > confidence_threshold+0.2 and keypoints[16][2] > confidence_threshold+0.2):
                print("yes33333")
                step +=1
                is_command_sounded = False
                f_reset_vars()
                f_send_data("1")
        except:
            pass
            #print("exception")
            #left_foot = keypoints[15]
            #right_foot = keypoints[16]

    
    """elif step == 3:
        if not is_command_sounded:
            #reproducir sonido
            reproduce_sound.f_easy_movenet(step+1)
            is_command_sounded = True

        print(abs(keypoints[9][1] - keypoints[10][1]))
        if abs(keypoints[9][1] - keypoints[10][1]) < 150 and keypoints[9][2] > confidence_threshold and keypoints[10][2] > confidence_threshold and i_clap<2:
            i_clap+=1
            print("yesss44444")
            time.sleep(0.5)
        
        if i_clap == 2:
            step += 1
            is_command_sounded = False
            f_reset_vars()
            ##### terminar el juego: enviar señal a la tablet que el juegop ya se acabo y cambiar la variable que recibe la señal de la tablet a ""
            f_send_data("1")"""

    #return keypoints


        

def f_medium(frame_received, confidence_threshold=0.1):
    global step, is_command_sounded, left_foot, right_foot, i_clap, is_game_finished

    #step = 2

    y, x, c = frame_received.shape
    keypoints_with_scores = f_read(frame_received)

    keypoints = np.squeeze(np.multiply(keypoints_with_scores, [y,x,1]))

    if step == 0:
        if not is_command_sounded:
            #reproducir sonido
            #reproduce_sound.f_movenet()
            reproduce_sound.f_med_movenet(step+1)
            print("hola")
            left_foot = None
            is_command_sounded = True
            #left_foot = keypoints[15]
            #right_foot = keypoints[16]
        
        try:
            if left_foot == None:
                if keypoints[15][2] > confidence_threshold and keypoints[16][2] > confidence_threshold:
                    left_foot = keypoints[15]
                    right_foot = keypoints[16]
        except:
            #print()
            pass
        

        try:
            #print(left_foot[0] - keypoints[15][0], "    ---------------------------      ", right_foot[0] - keypoints[16][0])
            #print(left_foot[0], " --------- ", keypoints[15][0], "    --------------      ", right_foot[0], " ---------------- ", keypoints[16][0], " ++++++++ ", keypoints[15][2], " ++++ ", keypoints[16][2])
            if (abs(left_foot[0] - keypoints[15][0]) > 30 or right_foot[0] - keypoints[16][0] > 30) and (keypoints[15][2] > confidence_threshold and keypoints[16][2] > confidence_threshold) and i_clap<2:
                print("yesssss")
                left_foot = keypoints[15]
                right_foot = keypoints[16]
                i_clap+=1

            
            if i_clap == 2:
                step += 1
                is_command_sounded = False
                i_clap = 0
                left_foot, right_foot = None
                                
        except:
            pass
            #print("exception")
            #left_foot = keypoints[15]
            #right_foot = keypoints[16]

    elif step == 1:

        if not is_command_sounded:
            #reproducir sonido
            reproduce_sound.f_med_movenet(step+1)
            is_command_sounded = True

        #if (keypoints[0][2] >= confidence_threshold and keypoints[10][2] >= confidence_threshold):
        #    print(abs(keypoints[0][1] - keypoints[10][1]), "****************** ", abs(keypoints[0][0] - keypoints[10][0]))

        if (abs(keypoints[0][1] - keypoints[10][1]) < 71 or abs(keypoints[0][0] - keypoints[10][0]) < 82) and (keypoints[0][2] >= confidence_threshold and keypoints[10][2] >= confidence_threshold):
            print("yesss222")
            step+=1
            is_command_sounded = False

    elif step == 2:
        
        if not is_command_sounded:
            #reproducir sonido
            reproduce_sound.f_med_movenet(step+1)
            is_command_sounded = True

        try:
            if left_foot == None:
                if keypoints[15][2] > confidence_threshold and keypoints[16][2] > confidence_threshold:
                    left_foot = keypoints[15]
                    right_foot = keypoints[16]
        except:
            #print()
            pass


        try:
            #print(left_foot[0] - keypoints[15][0], "    ---------------------------      ", right_foot[0] - keypoints[16][0])
            #if keypoints[15][2] > confidence_threshold:
            #    print(abs(left_foot[0] - keypoints[15][0]))

            if (abs(left_foot[0] - keypoints[15][0]) > 15 or right_foot[0] - keypoints[16][0] > 15) and (keypoints[15][2] > confidence_threshold and keypoints[16][2] > confidence_threshold) and i_clap<2:
                print("yesssss3333")
                time.sleep(1)
                left_foot = keypoints[15]
                right_foot = keypoints[16]
                i_clap+=1

            
            if i_clap == 2:
                step += 1
                f_reset_vars()
                ##### terminar el juego: enviar señal a la tablet que el juegop ya se acabo y cambiar la variable que recibe la señal de la tablet a ""
                f_send_data("completado")
                                
        except:
            pass
            #print("exception")
            #left_foot = keypoints[15]
            #right_foot = keypoints[16]


            
def f_hard(frame_received, confidence_threshold=0.4):
    global step, is_command_sounded, right_hand

    #step = 2

    keypoints = f_read(frame_received)

    if step == 0:

        if not is_command_sounded:
            #reproducir sonido
            reproduce_sound.f_movenet()
            reproduce_sound.f_dif_movenet(step+1)
            is_command_sounded = True


        try:
            if right_hand == None:
                if keypoints[9][2] > confidence_threshold:
                    right_hand = keypoints[9]
                    
        except:
            #print()
            pass        


        try:


            if abs(right_hand[0] - keypoints[9][0]) > 45 and keypoints[9][2] > confidence_threshold:
                print("yesssss")
                #time.sleep(1)
                step += 1
                is_command_sounded = False
                
                
                                
        except:
            pass

    elif step == 1:
        if not is_command_sounded:
            #reproducir sonido
            reproduce_sound.f_dif_movenet(step+1)
            is_command_sounded = True

        if ((abs(keypoints[14][0] - keypoints[9][0]) < 45 and abs(keypoints[14][1] - keypoints[9][1]) < 45) or (abs(keypoints[14][0] - keypoints[10][0]) < 30 and abs(keypoints[14][1] - keypoints[10][1]) < 30)) and (keypoints[14][2] > confidence_threshold and (keypoints[9][2] > confidence_threshold or keypoints[10][2] > confidence_threshold)):
            print("yesss22222")
            step+=1
            is_command_sounded = False

    elif step == 2:
        if not is_command_sounded:
            #reproducir sonido
            reproduce_sound.f_dif_movenet(step+1)
            is_command_sounded = True

        #print(abs(keypoints[1][0] - keypoints[10][0]), " ******************* ", )

        if ((abs(keypoints[1][0] - keypoints[10][0]) < 20 and abs(keypoints[1][1] - keypoints[10][1])) or (abs(keypoints[1][0] - keypoints[9][0]) < 20 and abs(keypoints[1][1] - keypoints[9][1])) <100) and (keypoints[1][2] > confidence_threshold and (keypoints[9][2] > confidence_threshold or keypoints[10][2] > confidence_threshold)):
            print("yessss33333333")
            #time.sleep(1)
            step += 1
            is_command_sounded = False
            f_reset_vars()
            ##### terminar el juego: enviar señal a la tablet que el juegop ya se acabo y cambiar la variable que recibe la señal de la tablet a ""
            f_send_data("completado")



def draw_connections(keypoints, edges, confidence_threshold):
    global frame

    y, x, c = frame.shape
    shaped = np.squeeze(np.multiply(keypoints, [y,x,1]))
    
    for edge, color in edges.items():
        p1, p2 = edge
        y1, x1, c1 = shaped[p1]
        y2, x2, c2 = shaped[p2]
        
        if (c1 > confidence_threshold) & (c2 > confidence_threshold):      
            cv2.line(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0,0,255), 2)    

def draw_keypoints(keypoints, confidence_threshold):
    global frame

    y, x, c = frame.shape
    shaped = np.squeeze(np.multiply(keypoints, [y,x,1]))
    
    #print(shaped)
    i=0
    for kp in shaped:
        ky, kx, kp_conf = kp
        if kp_conf > confidence_threshold:
            cv2.circle(frame, (int(kx), int(ky)), 4, (0,255,0), -1) 
            cv2.putText(frame, str(i), (int(kx), int(ky)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            print("hola")
        i+=1
    
        #print(i)

    #cv2.imshow('Video', frame)



if __name__ == "__main__":


    f_reset_vars()
    f_load_model()

    video_capture = cv2.VideoCapture(0, cv2.CAP_V4L2)
    #video_capture = cv2.VideoCapture(0)
    video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
    video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)
    i = 0

    

    while True:
        ret, frame = video_capture.read()
        #keypo = f_easy(frame)
        f_medium(frame)
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
        