import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    try:
        r = requests.get(url)
        data = r.json()
        temp = data['current_condition'][0]['temp_C']
        desc = data['current_condition'][0]['weatherDesc'][0]['value']
        print(f"\n🌍 {city.capitalize()}: {temp}°C and {desc}")
    except:
        print("\n❌ Could not find that city.")

while True:
    user_city = input("\nEnter city (or 'q' to quit): ")
    if user_city.lower() == 'q':
        break
    get_weather(user_city)
