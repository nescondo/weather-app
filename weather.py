import requests
from tkinter import *
from tkinter import ttk

# master frame (parent window)
root = Tk()
root.title("Weather Application")

# overall frame
content = ttk.Frame(root)

# country input label, input
country_label = ttk.Label(content, text="Hello! Please enter your country below:")
country_input = ttk.Entry(content)
content.grid(column=0, row=0)
country_label.grid(column=5, row=0)
country_input.grid(column=5, row=5)

countryContents = StringVar()
country_input["textvariable"] = countryContents

# thinking about how to collect user data inputted to input box from tk
class InputCollector:
	def __init__(self):
		user_input = ""
	
	def get_input(self, user_input):
		if user_input == "":
			
root.mainloop()

api_key = open('api_key.txt', 'r').read()
country = input("Please input country:\n")
lat = ''
lon = ''

# access coordinates of location
if country == "United States":
    city, state = input(f'Please input a city and state (city, state):\n').split(',')
    geocode = requests.get(
        f'http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&limit=1&appid={api_key}')
else:
    city = input("Please input a city:\n")
    geocode = requests.get(
        f'http://api.openweathermap.org/geo/1.0/direct?q={city},{country}&limit=1&appid={api_key}')

if geocode.status_code == requests.codes.ok:
    # print(geocode.text)
    loc = geocode.json()
    lat = loc[0]['lat']
    lon = loc[0]['lon']
    print(f'{lat}, {lon}')

weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}')
print(weather.text)

# access weather data
if weather.status_code == requests.codes.ok:
    data = weather.json()
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]

fahr_convert = int((temp - 273.15) * (9/5) + 32)
print(fahr_convert)







