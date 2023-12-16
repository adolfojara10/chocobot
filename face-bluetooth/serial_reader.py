import serial
import threading
import time
import sys

global received_data, ser

def f_start_vars():
    global received_data

    received_data = ""

class ReadLine:
    def __init__(self, s):
        self.buf = bytearray()
        self.s = s
        self.lock = threading.Lock()

    def readline(self):
        i = self.buf.find(b"\n")
        if i >= 0:
            r = self.buf[:i+1]
            self.buf = self.buf[i+1:]
            return r.decode('utf-8').strip()  # Decode and strip whitespace
        while True:
            i = max(1, min(2048, self.s.in_waiting))
            data = self.s.read(i)
            i = data.find(b"\n")
            if i >= 0:
                r = self.buf + data[:i+1]
                self.buf[0:] = data[i+1:]
                return r.decode('utf-8').strip()  # Decode and strip whitespace
            else:
                self.buf.extend(data)


def serial_reader():
    global received_data, ser
    max_retries = 3  # Maximum number of retry attempts
    
    while max_retries > 0:
        try:
            ser = serial.Serial('/dev/ttyTHS1', 9600)
            rl = ReadLine(ser)
            #ser.timeout = 1

            print("hola serial")

            if max_retries > 0:
                f_send_data("Bluetooth activado")

            while True:
                data = rl.readline()
                if data != "":
                    received_data = data
                    print(data)
                    sys.stdout.flush()
        except serial.SerialException as e:
            print("SerialException:", str(e))
            # Handle the exception as needed, e.g., log the error or other actions.
            max_retries -= 1  # Decrement the number of remaining retries
            if max_retries <= 0:
                print("Maximum retry attempts reached. Exiting.")
                break
            else:
                print(f"Retrying ({max_retries} retries remaining)...")
                time.sleep(1)  # Wait before attempting to reopen the serial port
        finally:
            ser.close()  # Close the serial port when done

def f_send_data(data_send):
    global ser

    #ser.flushInput() #This gives the bluetooth a little kick

    try:
        ser.write(str.encode(data_send))

        print("Done")
    except Exception as e:
        print("no se envian datos")
        print(e)