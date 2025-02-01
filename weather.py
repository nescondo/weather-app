import requests
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Weather Application")

frame = ttk.Frame(root, padding="3 3 12 12")
frame.grid(column=0, row=0, sticky=(N,W,E,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

country = StringVar()
country_entry = ttk.Entry(frame, width=7, textvariable=country)
country_entry.grid(column=2, row=1, sticky=(W,E))

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







