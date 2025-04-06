from flask import Flask, request, jsonify
from flask_cors import CORS
import webbrowser
import os
import threading

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

# Variable to store the latest location
current_location = [0, 0]

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

def open_index_html():
    # Get the absolute path to index.html
    html_file = os.path.join(os.path.dirname(__file__), 'getlocationh.html')

    # Open the HTML file in the default web browser, only if it's not already open
    current_url = 'file://' + os.path.realpath(html_file)
    webbrowser.open_new_tab(current_url)
    print('Opened URL:', current_url)

# This function will be run in a separate thread to open the browser in the background
def open_browser_in_background():
    open_index_html()  # Opens the browser or reuses the tab

def main():
    print("Starting server at http://127.0.0.1:5000")
    print("Opening index.html in the background...")

    # Open the browser in a non-blocking way
    open_browser_in_background()

    # Run the Flask app
    app.run(debug=True, use_reloader=False)  # Set use_reloader=False to prevent the server from starting twice

if __name__ == "__main__":
    main()
