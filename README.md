# WeatherAPI
This is a simple Python script that demonstrates how to use the OpenWeatherMap API to get the current weather for a given city.

##Prerequisites
- Python 3.x
- Requests library `pip install requests`
- OpenWeatherMap API key

## Usage
1. Clone this repository:
`git clone https://github.com/adit-dubey/WeatherAPI.git`
2. Open main.py in a text editor.
3. Replace YOUR_API_KEY with your OpenWeatherMap API key.
4. Save the file.
5. Run the script:
`python weather.py`
6. `Enter City:` enter the name of your city.

## Notes
- The OpenWeatherMap API requires an API key for authentication and authorization.
- You can get a free API key by signing up for an account on the <a href="https://openweathermap.org/"> OpenWeatherMap website.</a>
- The `params` dictionary in `main.py` contains the parameters that are sent with the API request.
- In this example, we are using the city parameter to specify the city, the `appid` parameter to provide our API key, and the `units` parameter to specify the temperature units (metric for Celsius or imperial for Fahrenheit).
- The response from the OpenWeatherMap API is returned in JSON format. 
- The `response.json()` method is used to parse the JSON and return a Python dictionary containing the data. 
- We can then access the relevant data fields using dictionary keys.
