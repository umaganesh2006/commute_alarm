import requests
import config

def get_coordinates(address):
    # 1. Convert "Times Square" -> "40.758,-73.985"
    base_url = "https://api.tomtom.com/search/2/geocode"
    encoded_addr = requests.utils.quote(address)
    url = f"{base_url}/{encoded_addr}.json?key={config.TOMTOM_API_KEY}"
    
    try:
        response = requests.get(url)
        data = response.json()
        # TomTom returns a list of results; we take the first one
        if data['results']:
            pos = data['results'][0]['position']
            return f"{pos['lat']},{pos['lon']}"
        return None
    except:
        return None

def get_commute_duration():
    # 2. Get traffic time between Home and Work
    start = get_coordinates(config.HOME_ADDRESS)
    end = get_coordinates(config.WORK_ADDRESS)
    
    if not start or not end:
        print("❌ Could not find address coordinates.")
        return 45 # Fallback

    # TomTom Routing API with traffic=true
    route_url = f"https://api.tomtom.com/routing/1/calculateRoute/{start}:{end}/json?key={config.TOMTOM_API_KEY}&traffic=true"
    
    try:
        response = requests.get(route_url)
        data = response.json()
        # Travel time is in seconds
        seconds = data['routes'][0]['summary']['travelTimeInSeconds']
        return int(seconds / 60)
    except Exception as e:
        print(f"❌ API Error: {e}")
        return 45

def get_weather_status():
    # Keep your existing OpenWeather logic (it works fine!)
    return "Clear" # (Or use your real OpenWeather code here)
    