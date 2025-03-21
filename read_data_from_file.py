def read_data_from_file(filename="car_Arduino_data.csv"):
    """
    Read data from the file and return it as a list of records.
    """
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
        return [line.strip().split(",") for line in lines]
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None

def print_file_data(data):
    """
    Print the data read from the file in a user-friendly format.
    """
    if data:
        for record in data:
            print(f"Limit Switch Status: {record[0]} {record[1]} {record[2]} {record[3]} {record[4]} {record[5]}")
            print(f"Temperature: {record[6]}°C, Gas Detected: {record[7]}, Motion Detected: {record[8]}")
    else:
        print("No data to display.")
