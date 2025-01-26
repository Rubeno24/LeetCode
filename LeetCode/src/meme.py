import requests

def get_weather(city, api_key):
    # URL to fetch weather data from WeatherAPI
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    
    try:
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            # Extracting the temperature in Celsius
            temp_c = data['current']['temp_c']
            condition = data['current']['condition']['text']  # Weather condition text
            
            # Convert Celsius to Fahrenheit
            temp_f = (temp_c * 9/5) + 32
            return temp_f, condition
        else:
            print(f"Error: Unable to fetch data (Status code: {response.status_code})")
            return None, None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None, None

def display_weather(temp_f, condition):
    if temp_f is not None and condition is not None:
        print(f"\nWeather Information:")
        print(f"Temperature: {temp_f:.2f}°F")  # Format the temperature to 2 decimal places
        print(f"Condition: {condition}")
    else:
        print("Couldn't fetch the weather data.")

def main():
    api_key = "76d6d2b20d2942fd9d843900252601"  # Replace with your WeatherAPI key
    city = input("Enter city name: ")
    
    temp_f, condition = get_weather(city, api_key)
    
    display_weather(temp_f, condition)

if __name__ == "__main__":
    main()
