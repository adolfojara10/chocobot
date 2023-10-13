from pyzbar.pyzbar import decode
import time
import serial_reader
import reproduce_sound

global i, is_command_sounded, start_time, end_time

def f_reset_vars():
    global i, is_command_sounded, start_time, end_time
    i = 0
    start_time = 0
    end_time = 0
    is_command_sounded = False

def f_easy(frame_received):
    global i, is_command_sounded, start_time, end_time

    print(str(i))

    if i == 0:
        if not is_command_sounded:
            start_time = time.time()
            #f_reproduce_command_sound(1)
            reproduce_sound.f_simon_dice()
            reproduce_sound.f_easy_simon(i)
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        if qr_code == "Aa":
            i+=1
            f_reproduce_posit_sound()
            is_command_sounded = False
        else:
            f_reproduce_reinforcement_sound()

    elif i ==1:
        if not is_command_sounded:
            #f_reproduce_command_sound(1)
            reproduce_sound.f_easy_simon(i)
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        if qr_code == "Ee":
            i+=1
            f_reproduce_posit_sound()
            is_command_sounded = False
        else:
            f_reproduce_reinforcement_sound()
            

    elif i ==2:
        if not is_command_sounded:
            #f_reproduce_command_sound(1)
            reproduce_sound.f_easy_simon(i)
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        if qr_code == "Ii":
            i+=1
            f_reproduce_posit_sound()
            is_command_sounded = False
        else:
            f_reproduce_reinforcement_sound()
            

    elif i ==3:
        if not is_command_sounded:
            #f_reproduce_command_sound(1)
            reproduce_sound.f_easy_simon(i)
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        if qr_code == "Oo":
            i+=1
            f_reproduce_posit_sound()
            is_command_sounded = False

        else:
            f_reproduce_reinforcement_sound()
            

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
            serial_reader.f_send_data(send_sms)
            #f_reproduce_final_sound()
            f_reset_vars()
            serial_reader.received_data = ""
        else:
            f_reproduce_reinforcement_sound()
            


    
    else: 
        pass



def f_medium(frame_received):
    global i, is_command_sounded, start_time, end_time

    print(str(i))

    if i == 0:
        if not is_command_sounded:
            #f_reproduce_command_sound(1)
            reproduce_sound.f_simon_dice()
            reproduce_sound.f_med_simon(i)
            start_time = time.time()
            
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        if qr_code == "Leon":
            i+=1
            f_reproduce_posit_sound()
            is_command_sounded = False
        else:
            f_reproduce_reinforcement_sound()

    elif i ==1:
        if not is_command_sounded:
            #f_reproduce_command_sound(1)
            reproduce_sound.f_med_simon(i)
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        if qr_code == "Cerdo":
            i+=1
            f_reproduce_posit_sound()
            is_command_sounded = False
        else:
            f_reproduce_reinforcement_sound()
            

    elif i ==2:
        if not is_command_sounded:
            #f_reproduce_command_sound(1)
            reproduce_sound.f_med_simon(i)
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        if qr_code == "Canguro":
            i+=1
            f_reproduce_posit_sound()
            is_command_sounded = False
        else:
            f_reproduce_reinforcement_sound()
            

    elif i ==3:
        if not is_command_sounded:
            #f_reproduce_command_sound(1)
            reproduce_sound.f_med_simon(i)
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        if qr_code == "Tortuga":
            i+=1
            f_reproduce_posit_sound()
            is_command_sounded = False

        else:
            f_reproduce_reinforcement_sound()

    elif i ==4:
        if not is_command_sounded:
            #f_reproduce_command_sound(1)
            reproduce_sound.f_med_simon(i)
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        if qr_code == "Guepardo":
            i+=1
            f_reproduce_posit_sound()
            is_command_sounded = False

        else:
            f_reproduce_reinforcement_sound()

    elif i ==5:
        if not is_command_sounded:
            #f_reproduce_command_sound(1)
            reproduce_sound.f_med_simon(i)
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        if qr_code == "Caballo":
            i+=1
            f_reproduce_posit_sound()
            is_command_sounded = False

        else:
            f_reproduce_reinforcement_sound()
    

    elif i ==6:
        if not is_command_sounded:
            #f_reproduce_command_sound(1)
            reproduce_sound.f_med_simon(i)
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        if qr_code == "Gallina":
            i+=1
            f_reproduce_posit_sound()
            is_command_sounded = False

        else:
            f_reproduce_reinforcement_sound()


    elif i ==7:
        if not is_command_sounded:
            #f_reproduce_command_sound(1)
            reproduce_sound.f_med_simon(i)
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        if qr_code == "Cabra":
            i+=1
            f_reproduce_posit_sound()
            is_command_sounded = False

        else:
            f_reproduce_reinforcement_sound()

    elif i ==8:
        if not is_command_sounded:
            #f_reproduce_command_sound(1)
            reproduce_sound.f_med_simon(i)
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        if qr_code == "Conejo":
            i+=1
            f_reproduce_posit_sound()
            is_command_sounded = False

        else:
            f_reproduce_reinforcement_sound()

    elif i == 9:
        if not is_command_sounded:
            #f_reproduce_command_sound(1)
            reproduce_sound.f_med_simon(i)
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        if qr_code == "Zorro":
            i+=1
            f_reproduce_posit_sound()
            is_command_sounded = False

        else:
            f_reproduce_reinforcement_sound()

    elif i == 10:
        if not is_command_sounded:
            #f_reproduce_command_sound(1)
            reproduce_sound.f_med_simon(i)
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        if qr_code == "Perro":
            i+=1
            f_reproduce_posit_sound()
            is_command_sounded = False

        else:
            f_reproduce_reinforcement_sound()

    elif i ==11:
        if not is_command_sounded:
            #f_reproduce_command_sound(1)
            reproduce_sound.f_med_simon(i)
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        if qr_code == "Caracol":
            end_time = time.time()
            total_time = int(end_time - start_time)
            send_sms = "1_" + total_time
            serial_reader.f_send_data(send_sms)
            i+=1
            #f_reproduce_final_sound()
            f_reset_vars()
            serial_reader.received_data = ""
        else:
            f_reproduce_reinforcement_sound()
            


    
    else: 
        pass

def f_hard(frame_received):
    global i, is_command_sounded, start_time, end_time

    print(str(i))

    if i == 0:
        if not is_command_sounded:
            #f_reproduce_command_sound(1)
            reproduce_sound.f_simon_dice()
            reproduce_sound.f_dif_simon(i)
            start_time = time.time()
            
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        if qr_code == "0":
            i+=1
            f_reproduce_posit_sound()
            is_command_sounded = False
        else:
            f_reproduce_reinforcement_sound()

    elif i ==1:
        if not is_command_sounded:
            #f_reproduce_command_sound(1)
            reproduce_sound.f_dif_simon(i)
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        if qr_code == "1":
            i+=1
            f_reproduce_posit_sound()
            is_command_sounded = False
        else:
            f_reproduce_reinforcement_sound()
            

    elif i ==2:
        if not is_command_sounded:
            #f_reproduce_command_sound(1)
            reproduce_sound.f_dif_simon(i)
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        if qr_code == "2":
            i+=1
            f_reproduce_posit_sound()
            is_command_sounded = False
        else:
            f_reproduce_reinforcement_sound()
            

    elif i ==3:
        if not is_command_sounded:
            #f_reproduce_command_sound(1)
            reproduce_sound.f_dif_simon(i)
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        if qr_code == "3":
            i+=1
            f_reproduce_posit_sound()
            is_command_sounded = False

        else:
            f_reproduce_reinforcement_sound()

    elif i ==4:
        if not is_command_sounded:
            #f_reproduce_command_sound(1)
            reproduce_sound.f_dif_simon(i)
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        if qr_code == "4":
            i+=1
            f_reproduce_posit_sound()
            is_command_sounded = False

        else:
            f_reproduce_reinforcement_sound()

    elif i ==5:
        if not is_command_sounded:
            #f_reproduce_command_sound(1)
            reproduce_sound.f_dif_simon(i)
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        if qr_code == "5":
            i+=1
            f_reproduce_posit_sound()
            is_command_sounded = False

        else:
            f_reproduce_reinforcement_sound()
    

    elif i ==6:
        if not is_command_sounded:
            #f_reproduce_command_sound(1)
            reproduce_sound.f_dif_simon(i)
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        if qr_code == "6":
            i+=1
            f_reproduce_posit_sound()
            is_command_sounded = False

        else:
            f_reproduce_reinforcement_sound()


    elif i ==7:
        if not is_command_sounded:
            #f_reproduce_command_sound(1)
            reproduce_sound.f_dif_simon(i)
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        if qr_code == "7":
            i+=1
            f_reproduce_posit_sound()
            is_command_sounded = False

        else:
            f_reproduce_reinforcement_sound()

    elif i ==8:
        if not is_command_sounded:
            #f_reproduce_command_sound(1)
            reproduce_sound.f_dif_simon(i)
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        if qr_code == "8":
            i+=1
            f_reproduce_posit_sound()
            is_command_sounded = False

        else:
            f_reproduce_reinforcement_sound()

    
    elif i ==9:
        if not is_command_sounded:
            #f_reproduce_command_sound(1)
            reproduce_sound.f_dif_simon(i)
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        if qr_code == "9":
            i+=1
            end_time = time.time()
            total_time = int(end_time - start_time)
            send_sms = "1_" + total_time
            serial_reader.f_send_data(send_sms)
            #f_reproduce_final_sound()
            f_reset_vars()
            serial_reader.received_data = ""
        else:
            f_reproduce_reinforcement_sound()
            


    
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

    # Check if a QR code was found and extract the data
    for obj in decoded_objects:
        qr_code_data = obj.data.decode('utf-8')
        print(f"QR Code Data: {qr_code_data}")

        return qr_code_data
