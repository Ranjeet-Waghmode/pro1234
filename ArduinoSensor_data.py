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
            "frontBonnet":     int(data[4]) ,
            "backBonnet":      int(data[5]) ,
            "temperature": float(data[6]),
            "gasDetected": bool(int(data[7])),
            "motionDetected": bool(int(data[8]))
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
        print(f"Front Bonnet: {data['frontBonnet']}")
        print(f"Back Bonnet: {data['backBonnet']}")
        print(f"Temperature: {data['temperature']:.2f} °C")
        print(f"Gas Detected: {data['gasDetected']}")
        print(f"Motion Detected: {data['motionDetected']}")
    else:
        print("Error: No data received.")
