import serial

ser = serial.Serial('COM3', 115200, timeout = 1)

ser.write(bytes('hello', encoding='ascii'))
ser.write(b'\x0d\x0a')

ser.write(bytes('12345', encoding='ascii'))
ser.write(b'\x0d\x0a')

ser.write(bytes('#$ABCDEFGH', encoding='ascii'))
ser.write(b'\x0d\x0a')

ser.close()

#PC-->MCU
#200130 : confirmed by Neo