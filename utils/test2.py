import serial

# Open the virtual COM4 port (created using com0com)
arduino = serial.Serial('COM4', 9600, timeout=1)

while True:
    # Read data from the port
    if arduino.in_waiting > 0:
        data = arduino.readline().decode('utf-8').strip()
        print(f"Received: {data}")
