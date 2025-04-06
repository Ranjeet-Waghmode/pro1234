from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

# Variable to store the latest location
current_location =[0,0]

@app.route('/')
def home():
    return "Server is running. Please open the HTML file in your browser."

@app.route('/location', methods=['POST'])
def receive_location():
    global current_location
    data = request.json
    current_location[0] = data.get("latitude")
    current_location[1] = data.get("longitude")
    print(f"Updated location: Latitude: {current_location[0]}, Longitude: {current_location[1]}")
    return jsonify({"status": "Location received", "location": current_location})

@app.route('/get_location', methods=['GET'])
def get_location():
    return jsonify(current_location)

if __name__ == "__main__":
    print("Starting server at http://127.0.0.1:5000")
    app.run(debug=True)
