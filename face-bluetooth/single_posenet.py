from jetson_inference import poseNet
from jetson_utils import videoSource, videoOutput, Log
from serial_reader import f_send_data
import reproduce_sound
import time

global net, step, is_command_sounded, left_foot, right_foot, i_clap, is_game_finished, right_hand

def f_reset_vars():
    global step, is_command_sounded, left_foot, right_foot, i_clap, is_game_finished, right_hand

    i_clap = 0
    step = 0
    is_command_sounded = False
    left_foot = None
    right_hand = None
    is_game_finished = False


def f_load_model():
    global net

    net = poseNet("resnet18-body", 0.15)


def f_detect(frame):

    # perform pose estimation (with overlay) - Replace with your pose estimation logic
    return net.Process(frame, overlay="links,keypoints")


def f_easy(frame_received, confidence_threshold=0.1):
    global step, is_command_sounded, left_foot, right_foot, i_clap, is_game_finished

    poses = f_detect(frame_received)

    print(str(step))

    if step == 0:

        if len(poses) > 0:

            if not is_command_sounded:
                #reproducir sonido
                #reproduce_sound.f_movenet()
                reproduce_sound.f_easy_movenet(step+1)
                is_command_sounded = True

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
                neck = poses[0].Keypoints[poses[0].FindKeypoint('neck')]
                left_elbow = poses[0].Keypoints[poses[0].FindKeypoint('left_elbow')]
                
                if left_wrist.x < neck.x or abs(left_wrist.y - left_elbow.y) < 40:
                    print("yessss")
                    step+=1
                    is_command_sounded = False

            elif rigth_wrist_idx > 0:
                rigth_wrist = poses[0].Keypoints[rigth_wrist_idx]
                neck = poses[0].Keypoints[poses[0].FindKeypoint('neck')]
                rigth_elbow = poses[0].Keypoints[poses[0].FindKeypoint('right_elbow')]
                
                if rigth_wrist.x > neck.x or abs(rigth_wrist.y - rigth_elbow.y) < 40:
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
                time.sleep(1.5)
                left_foot = None
                is_command_sounded = True
                #left_foot = keypoints[15]
                #right_foot = keypoints[16]
            
            try:
                if left_foot == None and poses[0].FindKeypoint('left_foot')>0:
                    left_foot = poses[0].Keypoints[poses[0].FindKeypoint('left_foot')]
                    right_foot = poses[0].Keypoints[poses[0].FindKeypoint('right_foot')]

            except:
                #print()
                pass
            

            try:
                #print(left_foot[0] - keypoints[15][0], "    ---------------------------      ", right_foot[0] - keypoints[16][0])
                #print(left_foot[0], " --------- ", keypoints[15][0], "    --------------      ", right_foot[0], " ---------------- ", keypoints[16][0], " ++++++++ ", keypoints[15][2], " ++++ ", keypoints[16][2])
                if (abs(left_foot.y - poses[0].Keypoints[poses[0].FindKeypoint('left_foot')]) > 20 or right_foot[0] - poses[0].Keypoints[poses[0].FindKeypoint('right_foot')] > 20):
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


        f_easy(img)
        # perform pose estimation (with overlay)
        """poses = f_detect(img)

        # print the pose results
        print("detected {:d} objects in image".format(len(poses)))

        print(poses[0].Keypoints)
        print(poses[0].ID)

        
        for pose in poses:
            print(pose)
            print(pose.Keypoints)
            print('Links', pose.Links)

        # render the image
        output.Render(img)"""

        # update the title bar
        output.SetStatus("{:s} | Network {:.0f} FPS".format("hhh", net.GetNetworkFPS()))

        # print out performance info
        net.PrintProfilerTimes()

        # exit on input/output EOS
        if not input.IsStreaming() or not output.IsStreaming():
            break


    """

    # create video sources & outputs
    video_capture = cv2.VideoCapture(0, cv2.CAP_V4L2)
    video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
    video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 360) # Replace 'args.input' with your video file or camera index


    # process frames until EOS or the user exits
    while True:
        # capture the next image
        ret, frame = video_capture.read()

        if not ret:  # check if the frame was read successfully
            break

        # print the pose results
        print("detected {:d} objects in image".format(len(poses)))

        for pose in poses:
            print(pose)
            print(pose.Keypoints)
            print('Links', pose.Links)

        # render the image - Replace with your rendering logic
        # output.Render(img)
        key = cv2.waitKey(1) & 0xFF

        # Hit 'q' on the keyboard to quit!
        if key == ord('q'):
                # Release handle to the webcam
            video_capture.release()
            cv2.destroyAllWindows()
            break
            
        cv2.imshow('Video', frame)"""

