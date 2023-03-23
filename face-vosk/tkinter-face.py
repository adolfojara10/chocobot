# Python program to open the
# camera in Tkinter
# Import the libraries,
# tkinter, cv2, Image and ImageTk

from tkinter import *
import cv2
from PIL import Image, ImageTk



# Declare the width and height in variables
width, height = 800, 600

# Set the width and height
#vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
#vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# Create a GUI app
app = Tk()

# Bind the app with Escape keyboard to
# quit app whenever pressed
app.bind('<Escape>', lambda e: app.quit())

app.geometry("720x720")

# Create a label and display it on app
label_widget = Label(app)
label_widget.pack()

def iniciar():
    pass

inicio = Button(app, text="Iniciar", command=iniciar)
inicio.place(x = 100, y = 580)

inputtxt = Text(app,
                   height = 5,
                   width = 20)

# Create a function to open camera and
# display it in the label_widget on app



def open_camera():

    # Define a video capture object
    vid = cv2.VideoCapture(0)

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
    label_widget.after(5, open_camera)


# Create a button to open the camera in GUI app
#button1 = Button(app, text="Open Camera", command=open_camera)
#button1.pack()

open_camera()
# Create an infinite loop for displaying app on screen
app.mainloop()
