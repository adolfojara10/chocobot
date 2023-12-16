from tracemalloc import start
from jetson_inference import poseNet
from jetson_utils import videoSource, videoOutput, Log
import jetson.utils
import serial_reader
import reproduce_sound
import time

global net, step, is_command_sounded, left_foot, right_foot, i_clap, is_game_finished, right_hand, start_time, end_time

def f_reset_vars():
    global step, is_command_sounded, left_foot, right_foot, i_clap, is_game_finished, right_hand, start_time, end_time

    i_clap = 0
    step = 0
    is_command_sounded = False
    left_foot = None
    right_hand = None
    is_game_finished = False
    start_time = 0
    end_time = 0


def f_load_model():
    global net

    net = poseNet("resnet18-body", 0.15)


def f_detect(frame):


    # perform pose estimation (with overlay) - Replace with your pose estimation logic
    return net.Process(jetson.utils.cudaFromNumpy(frame), overlay="links,keypoints")
    #return net.Process(frame, overlay="links,keypoints")


def f_easy(frame_received, confidence_threshold=0.1):
    global step, is_command_sounded, left_foot, right_foot, i_clap, is_game_finished, start_time, end_time

    poses = f_detect(frame_received)

    print(str(step))

    if step == 0:

        if len(poses) > 0:

            if not is_command_sounded:
                #reproducir sonido
                #reproduce_sound.f_movenet()
                reproduce_sound.f_easy_movenet(step+1)
                is_command_sounded = True
                start_time = time.time()

            print("0")
            left_wrist_idx = poses[0].FindKeypoint('left_wrist')
            left_elbow_idx = poses[0].FindKeypoint('left_elbow')
            rigth_wrist_idx = poses[0].FindKeypoint('right_wrist')
            rigth_elbow_idx = poses[0].FindKeypoint('right_elbow')

            if left_wrist_idx > 0:
                left_wrist = poses[0].Keypoints[left_wrist_idx]
                neck = poses[0].Keypoints[poses[0].FindKeypoint('neck')]
                nose = poses[0].Keypoints[poses[0].FindKeypoint('nose')]
                
                if left_wrist.y < neck.y or left_wrist.y <= nose.y:
                    print("yessss")
                    step+=1
                    time.sleep(0.5)
                    is_command_sounded = False
                

            elif left_elbow_idx > 0:
                left_elbow = poses[0].Keypoints[left_elbow_idx]
                neck = poses[0].Keypoints[poses[0].FindKeypoint('neck')]
                left_shoulder = poses[0].Keypoints[poses[0].FindKeypoint('left_shoulder')]
                
                if left_elbow.y <= left_shoulder.y or left_elbow.y <= neck.y:
                    print("yessss")
                    step+=1
                    is_command_sounded = False


            elif rigth_wrist_idx > 0:
                rigth_wrist = poses[0].Keypoints[rigth_wrist_idx]
                neck = poses[0].Keypoints[poses[0].FindKeypoint('neck')]
                nose = poses[0].Keypoints[poses[0].FindKeypoint('nose')]
                
                if rigth_wrist.y < neck.y or rigth_wrist.y <= nose.y:
                    print("yessss")
                    step+=1
                    is_command_sounded = False
                

            elif rigth_elbow_idx > 0:
                rigth_elbow = poses[0].Keypoints[rigth_elbow_idx]
                neck = poses[0].Keypoints[poses[0].FindKeypoint('neck')]
                left_shoulder = poses[0].Keypoints[poses[0].FindKeypoint('left_shoulder')]
                
                if rigth_elbow.y <= left_shoulder.y or rigth_elbow.y <= neck.y:
                    print("yessss")
                    step+=1
                    is_command_sounded = False

        """
        if (keypoints[9][0] < keypoints[0][0] and keypoints[10][0] < keypoints[0][0] and keypoints[9][2] > confidence_threshold and keypoints[0][2] > confidence_threshold and keypoints[10][2] > confidence_threshold):
            print("yessss")
            step+=1
            is_command_sounded = False"""

    elif step == 1:

        if len(poses) > 0:      
            print("1")
            if not is_command_sounded:
                #reproducir sonido
                reproduce_sound.f_easy_movenet(step+1)
                is_command_sounded = True

            left_wrist_idx = poses[0].FindKeypoint('left_wrist')
            rigth_wrist_idx = poses[0].FindKeypoint('right_wrist')
            
            if left_wrist_idx > 0:
                left_wrist = poses[0].Keypoints[left_wrist_idx]
                left_elbow = poses[0].Keypoints[poses[0].FindKeypoint('left_elbow')]
                rigth_elbow = poses[0].Keypoints[poses[0].FindKeypoint('right_elbow')]
                neck = poses[0].Keypoints[poses[0].FindKeypoint('neck')]
                rigth_wrist = poses[0].Keypoints[rigth_wrist_idx]

                if (abs(left_wrist.y - left_elbow.y) < 20 or abs(left_wrist.x - rigth_elbow.x) < 40 or abs(rigth_wrist.y - rigth_elbow.y) < 20 or abs(rigth_wrist.x - left_elbow.x) < 40) and (left_wrist.y > neck.y or rigth_wrist.y > neck.y) and (left_elbow.y > neck.y and rigth_elbow.y > neck.y):
                    print("yessss")
                    time.sleep(0.25)
                    step+=1
                    is_command_sounded = False

            elif rigth_wrist_idx > 0:
                left_wrist = poses[0].Keypoints[left_wrist_idx]
                left_elbow = poses[0].Keypoints[poses[0].FindKeypoint('left_elbow')]
                rigth_elbow = poses[0].Keypoints[poses[0].FindKeypoint('right_elbow')]
                neck = poses[0].Keypoints[poses[0].FindKeypoint('neck')]
                rigth_wrist = poses[0].Keypoints[rigth_wrist_idx]

                if (abs(left_wrist.y - left_elbow.y) < 20 or abs(left_wrist.x - rigth_elbow.x) < 40 or abs(rigth_wrist.y - rigth_elbow.y) < 20 or abs(rigth_wrist.x - left_elbow.x) < 40) and (left_wrist.y > neck.y or rigth_wrist.y > neck.y) and (left_elbow.y > neck.y and rigth_elbow.y > neck.y):
                    print("yessss")
                    step+=1
                    is_command_sounded = False
            
        """
        if ((abs(keypoints[9][0] - keypoints[8][0]) < 20 or abs(keypoints[9][1] - keypoints[8][1]) < 20 or abs(keypoints[7][0] - keypoints[9][0]) < 20) and (keypoints[9][2] >= confidence_threshold or keypoints[8][2] > confidence_threshold or keypoints[7][2] > confidence_threshold)) or ((abs(keypoints[10][0] - keypoints[7][0]) < 20 or abs(keypoints[10][1] - keypoints[7][1]) < 20 or abs(keypoints[10][0] - keypoints[8][0]) < 20) and (keypoints[10][2] >= confidence_threshold or keypoints[7][2] >= confidence_threshold or keypoints[8][2] >= confidence_threshold)):
            print("yesss2222")
            step+=1
            is_command_sounded = False"""

    elif step == 2:
        
        if len(poses) >0:
            if not is_command_sounded:
                #reproducir sonido
                reproduce_sound.f_easy_movenet(step+1)
                print("hola")
                #time.sleep(1.5)
                left_foot = None
                is_command_sounded = True
                #left_foot = keypoints[15]
                #right_foot = keypoints[16]
            
            try:
                if left_foot == None and poses[0].FindKeypoint('left_ankle')>0:
                    left_foot = poses[0].Keypoints[poses[0].FindKeypoint('left_ankle')]
                    right_foot = poses[0].Keypoints[poses[0].FindKeypoint('right_ankle')]

            except:
                #print()
                pass
            

            try:
                #print(left_foot[0] - keypoints[15][0], "    ---------------------------      ", right_foot[0] - keypoints[16][0])
                #print(left_foot[0], " --------- ", keypoints[15][0], "    --------------      ", right_foot[0], " ---------------- ", keypoints[16][0], " ++++++++ ", keypoints[15][2], " ++++ ", keypoints[16][2])
                if (abs(left_foot.y - poses[0].Keypoints[poses[0].FindKeypoint('left_ankle')].y) > 15 or right_foot[0] - poses[0].Keypoints[poses[0].FindKeypoint('right_ankle').y] > 15):
                    print("yes33333")
                    step +=1
                    is_command_sounded = False
                    
                    end_time = time.time()
                    total_time = int(end_time - start_time)
                    send_sms = "1_" + str(total_time)
                    serial_reader.f_send_data(send_sms)
                    f_reset_vars()
                    serial_reader.received_data = ""
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



def f_medium(frame_received, confidence_threshold=0.1):
    global step, is_command_sounded, left_foot, right_foot, i_clap, is_game_finished, start_time, end_time

    poses = f_detect(frame_received)

    print(str(step))

    if len(poses) > 0:
        if step == 0:
            if not is_command_sounded:
                #reproducir sonido
                #reproduce_sound.f_movenet()
                reproduce_sound.f_med_movenet(step+1)
                print("hola")
                left_foot = None
                is_command_sounded = True
                start_time = time.time()
                #left_foot = keypoints[15]
                #right_foot = keypoints[16]
            
            try:
                if left_foot == None and poses[0].FindKeypoint('left_ankle')>0:
                    left_foot = poses[0].Keypoints[poses[0].FindKeypoint('left_ankle')]
                    right_foot = poses[0].Keypoints[poses[0].FindKeypoint('right_ankle')]

            except:
                #print()
                pass
            

            try:
                #print(left_foot[0] - keypoints[15][0], "    ---------------------------      ", right_foot[0] - keypoints[16][0])
                #print(left_foot[0], " --------- ", keypoints[15][0], "    --------------      ", right_foot[0], " ---------------- ", keypoints[16][0], " ++++++++ ", keypoints[15][2], " ++++ ", keypoints[16][2])
                if (abs(left_foot.y - poses[0].Keypoints[poses[0].FindKeypoint('left_ankle')].y) > 20 or right_foot[0] - poses[0].Keypoints[poses[0].FindKeypoint('right_ankle').y] > 20) and i_clap<2:
                    print("***************************************")
                    print("***************************************")
                    print("***************************************")
                    print("***************************************")
                    print("yes")
                    left_foot = poses[0].Keypoints[poses[0].FindKeypoint('left_ankle')]
                    right_foot = poses[0].Keypoints[poses[0].FindKeypoint('right_ankle')]
                    i_clap+=1

                
                if i_clap == 2:
                    print("***************************************")
                    print("***************************************")
                    print("***************************************")
                    print("***************************************")
                    print("yes22222222222222222222222222")
                    step += 1
                    is_command_sounded = False
                    i_clap = 0
                    left_foot, right_foot = None
                    time.sleep(0.5)
                                    
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
            left_wrist_idx = poses[0].FindKeypoint('left_wrist')

            if left_wrist_idx > 0:
                left_wrist = poses[0].Keypoints[left_wrist_idx]
                neck = poses[0].Keypoints[poses[0].FindKeypoint('neck')]
                #left_shoulder = poses[0].Keypoints[poses[0].FindKeypoint('left_shoulder')]
                
                if (int(left_wrist.y - neck.y) < 40 and int(left_wrist.y - neck.y) > -40):
                    print("yessss")
                    step+=1
                    is_command_sounded = False

        elif step == 2:
            
            if not is_command_sounded:
                #reproducir sonido
                reproduce_sound.f_med_movenet(step+1)
                is_command_sounded = True

            try:
                if left_foot == None and poses[0].FindKeypoint('left_ankle')>0:
                    left_foot = poses[0].Keypoints[poses[0].FindKeypoint('left_ankle')]
                    right_foot = poses[0].Keypoints[poses[0].FindKeypoint('right_ankle')]

            except:
                #print()
                pass
            

            try:
                #print(left_foot[0] - keypoints[15][0], "    ---------------------------      ", right_foot[0] - keypoints[16][0])
                #print(left_foot[0], " --------- ", keypoints[15][0], "    --------------      ", right_foot[0], " ---------------- ", keypoints[16][0], " ++++++++ ", keypoints[15][2], " ++++ ", keypoints[16][2])
                if (abs(left_foot.y - poses[0].Keypoints[poses[0].FindKeypoint('left_ankle')].y) > 35 or right_foot[0] - poses[0].Keypoints[poses[0].FindKeypoint('right_ankle').y] > 35) and i_clap<2:
                    print("***************************************")
                    print("***************************************")
                    print("***************************************")
                    print("***************************************")
                    print("yes")
                    time.sleep(2.5)
                    #pass
                    #left_foot = poses[0].Keypoints[poses[0].FindKeypoint('left_ankle')]
                    #right_foot = poses[0].Keypoints[poses[0].FindKeypoint('right_ankle')]
                    i_clap+=1

                
                if i_clap == 2:
                    print("***************************************")
                    print("***************************************")
                    print("***************************************")
                    print("***************************************")
                    print("yes22222222222222222222222222")
                    step += 1
                    is_command_sounded = False
                    i_clap = 0
                    
                    end_time = time.time()
                    total_time = int(end_time - start_time)
                    send_sms = "1_" + str(total_time)
                    serial_reader.f_send_data(send_sms)
                    f_reset_vars()
                    serial_reader.received_data = ""
                                    
            except:
                pass
                #print("exception")
                #left_foot = keypoints[15]
                #right_foot = keypoints[16]


def f_hard(frame_received, confidence_threshold=0.4):
    global step, is_command_sounded, right_hand, start_time, end_time

    poses = f_detect(frame_received)

    print(str(step))

    if len(poses) > 0:
        if step == 0:

            if not is_command_sounded:
                #reproducir sonido
                #reproduce_sound.f_movenet()
                reproduce_sound.f_dif_movenet(step+1)
                is_command_sounded = True
                start_time = time.time()


            rigth_wrist_idx = poses[0].FindKeypoint('right_wrist')
            #rigth_elbow_idx = poses[0].FindKeypoint('right_elbow')

            if rigth_wrist_idx > 0:
                rigth_wrist = poses[0].Keypoints[rigth_wrist_idx]
                rigth_elbow = poses[0].Keypoints[poses[0].FindKeypoint('right_elbow')]
                rigth_shoulder = poses[0].Keypoints[poses[0].FindKeypoint('right_shoulder')]
                
                
                if rigth_wrist.y < rigth_elbow.y and abs(rigth_wrist.y - rigth_shoulder.y) < 50:
                    print("yessss")
                    step+=1
                    time.sleep(1)
                    is_command_sounded = False

        elif step == 1:
            if not is_command_sounded:
                #reproducir sonido
                reproduce_sound.f_dif_movenet(step+1)
                is_command_sounded = True

            rigth_wrist_idx = poses[0].FindKeypoint('right_wrist')
            left_knee_idx = poses[0].FindKeypoint('left_knee')

            if rigth_wrist_idx > 0 and left_knee_idx>0:
                rigth_wrist = poses[0].Keypoints[rigth_wrist_idx]
                left_knee = poses[0].Keypoints[poses[0].FindKeypoint('left_knee')]
                
                
                if abs(rigth_wrist.x - left_knee.x)<35:
                    print("yessss")
                    step+=1
                    time.sleep(0.5)
                    is_command_sounded = False

        elif step == 2:
            if not is_command_sounded:
                #reproducir sonido
                reproduce_sound.f_dif_movenet(step+1)
                is_command_sounded = True

            left_wrist_idx = poses[0].FindKeypoint('left_wrist')
            left_elbow_idx = poses[0].FindKeypoint('left_elbow')

            if left_wrist_idx > 0 and left_elbow_idx:
                left_wrist = poses[0].Keypoints[left_wrist_idx]
                left_elbow = poses[0].Keypoints[poses[0].FindKeypoint('left_elbow')]
                left_shoulder = poses[0].Keypoints[poses[0].FindKeypoint('left_shoulder')]
                
                if left_wrist.y < left_elbow.y and abs(left_shoulder.y - left_wrist.y)<35:
                    print("yessss")
                    step+=1
                    time.sleep(1)
                    is_command_sounded = False
                    end_time = time.time()
                    total_time = int(end_time - start_time)
                    send_sms = "1_" + str(total_time)
                    serial_reader.f_send_data(send_sms)
                    f_reset_vars()
                    serial_reader.received_data = ""



"""
if __name__ == "__main__":
    f_load_model()
    f_reset_vars()

        # create video sources & outputs
    input = videoSource("/dev/video0")
    output = videoOutput()

    # process frames until EOS or the user exits
    while True:
        # capture the next image
        img = input.Capture()

        if img is None: # timeout
            continue  


        #f_easy(img)
        #f_medium(img)
        f_hard(img)
        # perform pose estimation (with overlay)
        poses = f_detect(img)

        # print the pose results
        print("detected {:d} objects in image".format(len(poses)))

        #print(poses[0].Keypoints)
        #print(poses[0].ID)

        
        for pose in poses:
            print(pose)
            print(pose.Keypoints)
            print('Links', pose.Links)

        # render the image
        output.Render(img)

        # update the title bar
        output.SetStatus("{:s} | Network {:.0f} FPS".format("hhh", net.GetNetworkFPS()))

        # print out performance info
        net.PrintProfilerTimes()

        # exit on input/output EOS
        if not input.IsStreaming() or not output.IsStreaming():
            break

"""

