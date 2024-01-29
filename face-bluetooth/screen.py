"""import pylibi2c

# Open i2c device @/dev/i2c-0, addr 0x07.
i2c = pylibi2c.I2CDevice('/dev/i2c-1', 0x07)

# Open i2c device @/dev/i2c-0, addr 0x07, 8bits internal address
i2c = pylibi2c.I2CDevice('/dev/i2c-1', 0x07, iaddr_bytes=2)

# Set delay
i2c.delay = 10

# Set page_bytes
i2c.page_bytes = 16

# Set flags
i2c.flags = pylibi2c.I2C_M_IGNORE_NAK

# Python2
buf = bytes(bytearray(256))

# Python3
buf = bytes(256)

# Write data to i2c, buf must be read-only type
size = i2c.write(0x0, buf)"""


"""
from smbus2 import SMBus
import time

# Specify the I2C bus number (replace with the correct bus number)
bus_number = 2

# Specify the I2C address (replace with the correct address)
device_address = 0x50

# Create a 100x100 matrix filled with 255s
matrix_size = 100
data_matrix = [[255] * matrix_size for _ in range(matrix_size)]

# Flatten the matrix to a 1D list
data_list = [item for sublist in data_matrix for item in sublist]

# Create an SMBus object
with SMBus(bus_number) as bus:
    # Split the data into chunks of 32 bytes
    chunk_size = 32
    for i in range(0, len(data_list), chunk_size):
        chunk = data_list[i:i+chunk_size]
        bus.write_byte(device_address, 255)

        
        # Introduce a delay to allow the device to process the data
        time.sleep(0.1)

print(f"Sent data to {hex(device_address)}: {data_list}")"""


import time
import board
import math
import busio
#import terminalio
import displayio
from adafruit_display_text import label
import gc9a01

tft_clk  = board.SCK1
tft_mosi = board.MOSI1
tft_rst  = board.D18
tft_dc   = board.D25
tft_cs   = board.SPI_CS0
tft_bl   = board.D16
spi = busio.SPI(clock=tft_clk, MOSI=tft_mosi)


# Make the displayio SPI bus and the GC9A01 display
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_rst)
display = gc9a01.GC9A01(display_bus, width=240, height=240, backlight_pin=tft_bl)

# Make the main display context
main = displayio.Group()
display.show(main)

# Draw a text label
text = "Hello\nWorld!"
text_area = label.Label(text=text, color=0xFFFF00,
                        anchor_point=(0.5,0.5), anchored_position=(0,0))
text_group = displayio.Group(scale=2)
text_group.append(text_area) 
main.append(text_group)

# Animate the text 
theta = math.pi
r = 75
while True:
    print(time.monotonic(),"hello")
    text_group.x = 120 + int(r * math.sin(theta))
    text_group.y = 120 + int(r * math.cos(theta))
    theta -= 0.05
    time.sleep(0.01)
