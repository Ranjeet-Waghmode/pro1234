import requests

def get_weather_forecast(city_id): 

    # Construct the complete URL
# \    print(complete_url)
    # Make the request to the API
    response = requests.get(complete_url)
    
    # Check if the response status is OK (200)
    if response.status_code == 200:
        # Parse the JSON data       
        global weather_data 
        weather_data= response.json()
        
        # Extract relevant information
        city = weather_data["name"]
        country = weather_data["sys"]["country"]
        temp_kelvin = weather_data["main"]["temp"]
        
      


city_id = "1259229"  # Example: Moscow city ID
get_weather_forecast(city_id)

# Extract relevant information
city = "Pune" if weather_data["name"] == "Yerandwane" else weather_data["name"]
country = weather_data["sys"]["country"]
temp_kelvin = weather_data["main"]["temp"]
temp_celsius = temp_kelvin -273.15
temp_feels_like_celsius = weather_data["main"]["feels_like"]
weather_condition = weather_data["weather"][0]["description"]


# Print out the extracted data
print(f"City: {city}, {country}")
print(f"Weather Condition: {weather_condition}")
print(f"Temperature: {temp_celsius:.2f} °C (Feels Like: {temp_feels_like_celsius:.2f} °C)")
