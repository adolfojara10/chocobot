from pyzbar.pyzbar import decode
import time
import serial_reader
import reproduce_sound
import cv2

global i, is_command_sounded, start_time, end_time

def f_reset_vars():
    global i, is_command_sounded, start_time, end_time
    i = 0
    start_time = 0
    end_time = 0
    is_command_sounded = False

def f_easy(frame_received):
    global i, is_command_sounded, start_time, end_time

    #print(str(i))

    if i == 0:
        if not is_command_sounded:
            start_time = time.time()
            #f_reproduce_command_sound(1)
            #reproduce_sound.f_simon_dice()
            reproduce_sound.f_easy_simon(i)
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        print(qr_code)
        if qr_code == "Aa":
            i+=1
            #i+=4
            #f_reproduce_posit_sound()
            is_command_sounded = False
        else:
            #f_reproduce_reinforcement_sound()
            pass

    elif i ==1:
        if not is_command_sounded:
            #f_reproduce_command_sound(1)
            reproduce_sound.f_easy_simon(i)
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        if qr_code == "Ee":
            i+=1
            #f_reproduce_posit_sound()
            is_command_sounded = False
        else:
            #f_reproduce_reinforcement_sound()
            pass
            

    elif i ==2:
        if not is_command_sounded:
            #f_reproduce_command_sound(1)
            reproduce_sound.f_easy_simon(i)
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        if qr_code == "Ii":
            i+=1
            #f_reproduce_posit_sound()
            is_command_sounded = False
        else:
            #f_reproduce_reinforcement_sound()
            pass
            

    elif i ==3:
        if not is_command_sounded:
            #f_reproduce_command_sound(1)
            reproduce_sound.f_easy_simon(i)
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        if qr_code == "Oo":
            i+=1
            #f_reproduce_posit_sound()
            is_command_sounded = False

        else:
            #f_reproduce_reinforcement_sound()
            pass
            

    elif i ==4:
        if not is_command_sounded:
            #f_reproduce_command_sound(1)
            reproduce_sound.f_easy_simon(i)
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        if qr_code == "Uu":
            i+=1
            end_time = time.time()
            total_time = int(end_time - start_time)
            send_sms = "1_" + str(total_time)
            #serial_reader.received_data = "good"
            serial_reader.f_send_data(send_sms)
            #reproduce_sound.f_good("simon_dice_facil")
            time.sleep(1)
            serial_reader.received_data = ""
            f_reset_vars()
            
        else:
            #f_reproduce_reinforcement_sound()
            pass
            


    
    else: 
        pass



def f_medium(frame_received):
    global i, is_command_sounded, start_time, end_time

    #print(str(i))

    if i == 0:
        if not is_command_sounded:
            #f_reproduce_command_sound(1)
            #reproduce_sound.f_simon_dice()
            reproduce_sound.f_med_simon(i)
            start_time = time.time()
            
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        if qr_code == "Leon":
            i+=1
            #f_reproduce_posit_sound()
            is_command_sounded = False
        else:
            #f_reproduce_reinforcement_sound()
            pass

    elif i ==1:
        if not is_command_sounded:
            #f_reproduce_command_sound(1)
            reproduce_sound.f_med_simon(i)
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        if qr_code == "Tortuga":
            i+=1
            #f_reproduce_posit_sound()
            is_command_sounded = False
        else:
            #f_reproduce_reinforcement_sound()
            pass
            

    elif i ==2:
        if not is_command_sounded:
            #f_reproduce_command_sound(1)
            reproduce_sound.f_med_simon(i)
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        if qr_code == "Zorro":
            i+=1
            #f_reproduce_posit_sound()
            is_command_sounded = False
        else:
            #f_reproduce_reinforcement_sound()
            pass
            

    elif i ==3:
        if not is_command_sounded:
            #f_reproduce_command_sound(1)
            reproduce_sound.f_med_simon(i)
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        if qr_code == "Guepardo":
            i+=1
            #f_reproduce_posit_sound()
            is_command_sounded = False

        else:
            #f_reproduce_reinforcement_sound()
            pass

    elif i ==4:
        if not is_command_sounded:
            #f_reproduce_command_sound(1)
            reproduce_sound.f_med_simon(i)
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        if qr_code == "Canguro":
            i+=1
            end_time = time.time()
            total_time = int(end_time - start_time)
            send_sms = "1_" + str(total_time)
            #serial_reader.received_data = "good"
            serial_reader.f_send_data(send_sms)
            #reproduce_sound.f_good("simon_dice_facil")
            time.sleep(1)
            serial_reader.received_data = ""
            f_reset_vars()
            
        else:
            #f_reproduce_reinforcement_sound()
            pass

    else: 
        pass



def f_hard(frame_received):
    global i, is_command_sounded, start_time, end_time

    #print(str(i))

    if i == 0:
        if not is_command_sounded:
            #f_reproduce_command_sound(1)
            #reproduce_sound.f_simon_dice()
            reproduce_sound.f_dif_simon(i)
            start_time = time.time()
            
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        if qr_code == "1":
            i+=1
            #f_reproduce_posit_sound()
            is_command_sounded = False
        else:
            #f_reproduce_reinforcement_sound()
            pass

    elif i ==1:
        if not is_command_sounded:
            #f_reproduce_command_sound(1)
            reproduce_sound.f_dif_simon(i)
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        if qr_code == "2":
            i+=1
            #f_reproduce_posit_sound()
            is_command_sounded = False
        else:
            #f_reproduce_reinforcement_sound()
            pass
            

    elif i ==2:
        if not is_command_sounded:
            #f_reproduce_command_sound(1)
            reproduce_sound.f_dif_simon(i)
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        if qr_code == "3":
            i+=1
            #f_reproduce_posit_sound()
            is_command_sounded = False
        else:
            #f_reproduce_reinforcement_sound()
            pass
            

    elif i ==3:
        if not is_command_sounded:
            #f_reproduce_command_sound(1)
            reproduce_sound.f_dif_simon(i)
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        if qr_code == "4":
            i+=1
            #f_reproduce_posit_sound()
            is_command_sounded = False

        else:
            #f_reproduce_reinforcement_sound()
            pass

    elif i ==4:
        if not is_command_sounded:
            #f_reproduce_command_sound(1)
            reproduce_sound.f_dif_simon(i)
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        if qr_code == "5":
            i+=1
            end_time = time.time()
            total_time = int(end_time - start_time)
            send_sms = "1_" + str(total_time)
            #serial_reader.received_data = "good"
            serial_reader.f_send_data(send_sms)
            #reproduce_sound.f_good("simon_dice_facil")
            time.sleep(1)
            serial_reader.received_data = ""
            f_reset_vars()
            
        else:
            #f_reproduce_reinforcement_sound()
            pass        


    
    else: 
        pass

def f_reproduce_command_sound(level):
    pass

def f_reproduce_reinforcement_sound():
    pass


def f_reproduce_posit_sound():
    pass

def f_reproduce_final_sound():
    pass


def f_read_qr(frame_received):
    # Decode QR code(s) from the frame
    decoded_objects = decode(frame_received)
    print(decoded_objects)
    # Check if a QR code was found and extract the data
    for obj in decoded_objects:
        qr_code_data = obj.data.decode('utf-8')
        print(f"QR Code Data: {qr_code_data}")

        return qr_code_data



"""
if __name__ == "__main__":


    f_reset_vars()
    #f_load_model()

    video_capture = cv2.VideoCapture(0, cv2.CAP_V4L2)
    #video_capture = cv2.VideoCapture(0)
    video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
    video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)
    #i = 0

    

    while True:
        ret, frame = video_capture.read()
        frame2 = cv2.flip(frame, 0)
        frame2 = cv2.flip(frame2, 1)
        #f_easy(frame)
        f_hard(frame2)
        key = cv2.waitKey(1) & 0xFF

        # Hit 'q' on the keyboard to quit!
        if key == ord('q'):
                # Release handle to the webcam
            video_capture.release()
            cv2.destroyAllWindows()
            #delete_files()
            #serial_thread.join()
            break
        cv2.imshow('Video', frame)"""