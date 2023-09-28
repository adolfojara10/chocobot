from pyzbar.pyzbar import decode

global i, is_command_sounded

def f_reset_vars():
    global i, is_command_sounded
    i = 0
    is_command_sounded = False

def f_easy(frame_received):
    global i, is_command_sounded

    print(str(i))

    if i == 0:
        if not is_command_sounded:
            f_reproduce_command_sound(1)
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
            f_reproduce_command_sound(1)
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
            f_reproduce_command_sound(1)
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
            f_reproduce_command_sound(1)
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
            f_reproduce_command_sound(1)
            is_command_sounded = True

        qr_code = f_read_qr(frame_received)
        if qr_code == "Uu":
            i+=1
            f_reproduce_final_sound()
            f_reset_vars()
        else:
            f_reproduce_reinforcement_sound()
            


    
    else: 
        pass



def f_medium(frame_received):
    pass

def f_hard(frame_received):
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
