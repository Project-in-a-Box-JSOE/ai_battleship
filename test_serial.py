import serial

def test_serial() :

   with serial.Serial('/dev/tty.usbmodem1421', 9600, timeout=1) as arduino:

   # arduino = serial.Serial("/dev/tty.usbmodem1421", 9600) #ser is the variable that will be communicating with the arduino
   # print(b'hi')
      print(arduino.name)

      for x in range(1,3):
         if(arduino.is_open):
            x = arduino.readline()
            print(x)

      print("wrote ", arduino.write('billy'.encode()), " bytes")
      #print("wrote ", arduino.write('1'.encode()), " bytes")

      
      for x in range(1,50):
         if(arduino.is_open):
            x = arduino.readline()
            print(x)      
   return

if __name__ == "__main__":
   test_serial()

# #first param is port
# #second param is baud rate that needs to match arduino sketch defatul is 9600 but we can speed it up (its bps - bits per second)


# # d = struct.pack('<I', number)       # pack integer data as little-edian bytes
# # print("struct complete\n")

# #a-j = 0-9
# #xyz = hit/miss/boat

#    #arduino.write('b'.encode())

# #print('z'.encode())
# #arduino.write('1'.encode())
# #arduino.write('h'.encode())

# xVal = '0'
# #xByte = str.encode(xVal)
# yVal = '5'
# hms = 'h' #hit/miss/ship
# arduino.write(xVal.encode())
# #arduino.write(xVal)
# print(xVal.encode())