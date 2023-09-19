import serial

# Define the serial port
serial_port = "/dev/ttyTHS1"

# Define the baud rate (adjust to match your device's settings)
baud_rate = 9600

try:
    # Open the serial port
    ser = serial.Serial(serial_port, baud_rate)
    print(f"Serial port {serial_port} opened successfully.")

    while True:
        # Read data from the serial port
        data = ser.readline().decode("utf-8").strip()
        if data:
            print(f"Received: {data}")
        
        if data == "exit":
            break

except serial.SerialException as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Close the serial port when done
    if ser.is_open:
        ser.close()
        print(f"Serial port {serial_port} closed.")


