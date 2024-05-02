import requests

API_KEY = ""

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

cont = True
city = input("Enter a city name: ")

while cont:

    request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
    response = requests.get(request_url)

    if response.status_code == 200 :
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = round(data['main']['temp'] - 273.15,2)

        print("Weather: ",weather)
        print("Temperature: ", temperature, "celsius")
    else:    
        print("Error occured.")

    city = input("Enter another city name or press q to quit ")

    if city.lower() == "q":
        cont = False
        print("You quit")
