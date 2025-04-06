import serial
import time

# Set up the serial communication with the Arduino (adjust port and baud rate as needed)
arduino = serial.Serial('COM3', 9600, timeout=1)

def request_data():
    """
    Send a request to Arduino and return the response as a list of values.
    """
    arduino.write(b'R')  # 'R' to request data from Arduino

    # Wait for a response from Arduino
    time.sleep(1)

    # Read data from Arduino
    response = arduino.readline().decode('utf-8').strip()
    if response:
        return response.split(',')
    else:
        return None

def save_data_to_file(data, filename="car_Arduino_data.csv"):
    """
    Save the received data to a file.
    """
    with open(filename, "a") as f:
        f.write(",".join(str(val) for val in data) + "\n")

def get_live_data():
    """
    Get the latest data from Arduino and return it as a dictionary.
    """
    data = request_data()
    if data:
        car_status = {
            "frontLeftDoor":   int(data[0]),
            "frontRightDoor":  int(data[1]) ,
            "backLeftDoor":    int(data[2]),
            "backRightDoor":   int(data[3]),
            "Bonnet":     int(data[4]) ,
            "Trunk":      int(data[5]) ,
            "temperature": float(data[6]),
            "gasDetected": bool(int(data[7])),
            "motionDetected": bool(int(data[8])),
            "lat": float(data[9]),
            "long": float(data[10]),
            "speed": float(data[11]),
            "rpm": float(data[12]),
            "fuel": float(data[13]),
            "voltage": float(data[14]),
            "current": float(data[15]),
            "mpu_ax": float(data[16]),
            "mpu_ay": float(data[17]),
            "mpu_az": float(data[18]),
            "mpu_gx": float(data[19]),
            "mpu_gy": float(data[20]),  
            "mpu_gz": float(data[21]),
            "mpu_x": float(data[22]),
            "mpu_y": float(data[23]),
            "mpu_z": float(data[24]),
            
        }
        return car_status
    else:
        return None

def print_data(data):
    """
    Print the received data in a user-friendly format.
    """
    if data:
        print("Limit Switch Status:")
        print(f"Front Left Door: {data['frontLeftDoor']}")
        print(f"Front Right Door: {data['frontRightDoor']}")
        print(f"Back Left Door: {data['backLeftDoor']}")
        print(f"Back Right Door: {data['backRightDoor']}")
        print(f"Bonnet: {data['Bonnet']}")
        print(f"Trunk: {data['Trunk']}")
        print(f"Temperature: {data['temperature']:.2f} °C")
        print(f"Gas Detected: {data['gasDetected']}")
        print(f"Motion Detected: {data['motionDetected']}")
        print("GPS Data:")
        print(f"Latitude: {data['lat']}")
        print(f"Longitude: {data['lon']}")
        print(f"Speed: {data['speed']} km/h")
        print(f"RPM: {data['rpm']}")
        print(f"Fuel Level: {data['fuel']}%")
        print(f"Voltage: {data['voltage']} V")
        print(f"Current: {data['current']} A")
        print("MPU Data:")
        print(f"Accelerometer (X, Y, Z): ({data['mpu_ax']}, {data['mpu_ay']}, {data['mpu_az']})")
        print(f"Gyroscope (X, Y, Z): ({data['mpu_gx']}, {data['mpu_gy']}, {data['mpu_gz']})")
        print(f"MPU Position (X, Y, Z): ({data['mpu_x']}, {data['mpu_y']}, {data['mpu_z']})")
        print("Data saved to file.")
       
    else:
        print("Error: No data received.")
