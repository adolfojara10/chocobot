import tkinter as tk
import cv2
from PIL import Image, ImageTk
import threading as th
import time

global run_thread, root, value1, value2, save_name
run_thread = False
save_name = False

def save_inputs():
    global value1, value2, save_name, root
    # Get the values from the text inputs and save them
    value1 = entry1.get()
    value2 = entry2.get()
    print(f"Value 1: {value1}, Value 2: {value2}")

    save_name = True

    root.destroy()

    #return value1, value2

def return_name_values():
    global value1, value2

    return value1, value2

def create_widgets():
    global root
    # Create a label and text input for the first field
    global label1, entry1
    label1 = tk.Label(root, text="Nombre(s):")
    label1.pack()

    entry1 = tk.Entry(root)
    entry1.pack()

    # Create a label and text input for the second field
    global label2, entry2
    label2 = tk.Label(root, text="Apellidos:")
    label2.pack()

    entry2 = tk.Entry(root)
    entry2.pack()

    global label_widget
    label_widget = tk.Label(root)
    label_widget.pack()

    # Create a button to save the inputs
    global button
    button = tk.Button(root, text="Guardar alumno", command=save_inputs)
    button.pack()

def open_camera():

    global vid, run_thread

    

    # Capture the video frame by frame
    ret, frame = vid.read()

    frame = cv2.flip(frame, 1)

    # Convert image from one color space to other
    opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

    # Capture the latest frame and transform to image
    captured_image = Image.fromarray(opencv_image)

    # Convert captured image to photoimage
    photo_image = ImageTk.PhotoImage(image=captured_image)

    # Displaying photoimage in the label
    label_widget.photo_image = photo_image

    # Configure image in the label
    label_widget.configure(image=photo_image)

    # Repeat the same process after every 10 seconds
    label_widget.after(10, open_camera)

    

def start():
    global root, vid, run_thread, value1, value2, save_name

    save_name = False
    value1=""
    value2=""


    run_thread=True

    # Define a video capture object
    #vid = cv2.VideoCapture(0)

    root = tk.Tk()

    root.geometry("700x700")

    #t_camera = th.Thread(target=open_camera)
    #t_window = th.Thread(target=root.mainloop)


    

    create_widgets()
    #t_camera.start()
    #t_window.start()
    root.mainloop()
"""
def change_state_thread(state):
    global run_thread, root
    run_thread = state
    if run_thread==False:
        root.quit()
"""

"""if __name__ == '__main__':
    t_start = th.Thread(target=start)
    t_start.start()"""
    #start()
    #time.sleep(6)
    #print("hola")
    #change_state_thread(False)


