import serial

class ReadLine:
    def __init__(self, s):
        self.buf = bytearray()
        self.s = s

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

ser = serial.Serial('/dev/ttyTHS1', 9600)
rl = ReadLine(ser)
ser.timeout = 1

while True:
    print(rl.readline())
