import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
import smtplib
from email.mime.text import MIMEText
import os

# --- 1. Load and Preprocess Data ---
def load_and_preprocess_data(file_path):
    # Load the CSV file containing sensor data
    data = pd.read_csv(file_path)

    # Handle missing values (forward fill to replace NaN values)
    # data.fillna(method='ffill', inplace=True)

    # Feature Engineering
    # Door activity: Count the number of door/badge open states
    data['doorActivity'] = (data['frontLeftDoor'] + data['frontRightDoor'] + 
                            data['backLeftDoor'] + data['backRightDoor'] + 
                            data['Bonnet'] + data['Trunk'])
    
    # Movement frequency: Calculate the frequency of motion detections over a rolling window (e.g., 10 minutes)
    data['movementFrequency'] = data['motionDetected'].rolling(window=5).sum()
    
    # Standardize/normalize numeric features
    features = ['frontLeftDoor', 'frontRightDoor', 'backLeftDoor', 'backRightDoor', 'Bonnet', 
                'Trunk', 'temperature', 'gasDetected', 'motionDetected', 'lat', 'lon', 'speed',
                'rpm', 'fuel', 'voltage', 'current', 'mpu_ax', 'mpu_ay', 'mpu_az', 'mpu_gx', 'mpu_gy', 
                'mpu_gz', 'mpu_x', 'mpu_y', 'mpu_z', 'doorActivity', 'movementFrequency']
    
    X = data[features]

    # Normalize the features (important for machine learning models)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, data

# --- 2. Train the Anomaly Detection Model ---
def train_anomaly_detection_model(X_scaled):
    # Train an Isolation Forest model for anomaly detection
    model = IsolationForest(n_estimators=100, contamination=0.1)  # 10% expected outliers
    model.fit(X_scaled)
    return model

# --- 3. Detect Anomalies ---
def detect_anomalies(model, X_scaled, data):
    # Predict anomalies (1 = normal, -1 = anomaly)
    data['anomaly'] = model.predict(X_scaled)

    # Filter the anomalies
    anomalies = data[data['anomaly'] == -1]  # 0 indicates an anomaly in Isolation Forest
    
    return anomalies

# --- 4. Alert System (Email Notification) ---
def send_alert():
    from_email = "your_email@example.com"
    to_email = "user_email@example.com"
    subject = "Vehicle Theft Alert!"
    body = "Unusual activity detected around your vehicle. Please check immediately."

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    # Send the email
    try:
        with smtplib.SMTP('smtp.example.com') as server:
            server.login('your_email@example.com', 'password')
            server.sendmail(from_email, to_email, msg.as_string())
            print("Alert sent!")
    except Exception as e:
        print(f"Failed to send alert: {e}")

# --- 5. Main Function to Run the System ---
def run_theft_detection_system(file_path):
    global theft_detection_status 

    # Step 1: Load and preprocess the data
    X_scaled, data = load_and_preprocess_data(file_path)
    
    # Step 2: Train the anomaly detection model
    model = train_anomaly_detection_model(X_scaled)
    
    # Step 3: Detect anomalies in the data
    anomalies = detect_anomalies(model, X_scaled, data)
    
    # If anomalies are detected, trigger the alert system
    if not anomalies.empty:
        print("Anomalies detected! Triggering alerts.")
        # send_alert()
        # Optionally, save the anomalies to a separate CSV for further review
        anomalies.to_csv(os.path.join(os.path.dirname(os.path.abspath("Start___app.py")),"data", 'detected_anomalies.csv') , index=False)
        theft_detection_status = True

    else:
        print("No anomalies detected. Vehicle seems secure.")
        theft_detection_status = False


# --- 6. Run the System (Replace with the actual file path of your CSV) ---
def theft_detection_main():
    run_theft_detection_system(file_path = os.path.join(os.path.dirname(os.path.abspath("Start___app.py")),"data", "car_Arduino_data.csv"))
    # print(theft_detection_status)
    return theft_detection_status
if __name__ == "__main__":
   theft_detection_main()