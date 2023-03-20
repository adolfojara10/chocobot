import cv2
import tkinter as tk
from PIL import Image, ImageTk

class CameraWindow:

    def __init__(self, master):
        self.master = master
        self.cap = cv2.VideoCapture(0)
        self.create_widgets()

    def create_widgets(self):
        # Create a canvas to display the camera feed
        self.canvas = tk.Canvas(self.master, width=640, height=480)
        self.canvas.pack(side=tk.LEFT)

        # Create two text inputs and a button to save on the right
        self.frame = tk.Frame(self.master)
        self.frame.pack(side=tk.RIGHT, padx=10, pady=10)

        self.label1 = tk.Label(self.frame, text="Input 1:")
        self.label1.pack()

        self.entry1 = tk.Entry(self.frame)
        self.entry1.pack()

        self.label2 = tk.Label(self.frame, text="Input 2:")
        self.label2.pack()

        self.entry2 = tk.Entry(self.frame)
        self.entry2.pack()

        self.button = tk.Button(self.frame, text="Save")
        self.button.pack()

        # Start the camera feed
        self.update()

    def update(self):
        # Get a frame from the camera
        ret, frame = self.cap.read()

        # Convert the frame from BGR to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Convert the image to a PIL ImageTk object
        photo = ImageTk.PhotoImage(image=Image.fromarray(image))

        # Display the image on the canvas
        self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)

        # Call this function again after 15 milliseconds
        self.canvas.after(15, self.update)

if __name__ == '__main__':
    root = tk.Tk()
    app = CameraWindow(root)
    root.mainloop()

