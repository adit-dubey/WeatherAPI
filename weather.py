import requests

# Set API endpoint and parameters
url = "http://api.openweathermap.org/data/2.5/weather"
params = {
    "city": input("Enter City:"),
#   Generate your own Api Key
    "appid": "4274e8d7549993652387d6efd89d16bb",
    "units": "metric"
}

# Make a GET request to the API
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code != 200:
    print("Error:", response.json()["message"])
else:
    # Parse the response JSON
    data = response.json()

    # Print the current weather for the city
    print(f"Weather in {data['name']}: {data['weather'][0]['description']}, {data['main']['temp']}°C")
