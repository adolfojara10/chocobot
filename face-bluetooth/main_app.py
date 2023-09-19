from serial_reader import serial_reader
import threading


if __name__ == "__main__":
    # Create a thread for serial communication
    serial_thread = threading.Thread(target=serial_reader)

    # Start the serial communication thread
    serial_thread.start()