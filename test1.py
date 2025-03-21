import serial
import time

# Open the virtual COM3 port (created using com0com)
arduino = serial.Serial('COM3', 9600, timeout=1)

while True:
    # Send some test data
    arduino.write(b'Hello from COM3!\n')
    time.sleep(1)  # Wait for 1 second
