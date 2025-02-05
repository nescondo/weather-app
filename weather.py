import requests
from tkinter import *
from tkinter import ttk

# master frame (parent window)
root = Tk()
root.title("Weather Application")

# overall frame
content = ttk.Frame(root)

# country input label, input
location = StringVar()
loc_label = ttk.Label(content, text="Enter location (city, state (if applicable), country): ")
loc_input = ttk.Entry(content, textvariable=location)
content.grid(column=0, row=0)
loc_label.grid(column=5, row=0)
loc_input.grid(column=5, row=5)

# thinking about how to collect user data inputted to input box from tk
class InputCollector:
	def __init__(self, entry):
		self.inputs = []
		self.entry = entry.get()
	
	def store_inputs(self):
		# still need to account for potential space at end (or any other invalid inputs)
		i = 0
		self.inputs = self.entry.split(",")
		# removes all spaces and beginning of word
		for data in self.inputs:
			if data[0] == " ":
				new_string = data[1:]
				self.inputs[i] = new_string
			# checks if all spaces have been removed
			if i > 0 and data[0] == "":
				break
			i += 1

	def get_inputs(self):
		return self.inputs
		
			
root.mainloop()
user_loc = InputCollector(location)
user_loc.store_inputs()
print(f'Current inputs {user_loc.get_inputs()}')
api_key = open('api_key.txt', 'r').read()
country = input("please input country:\n")
lat = ''
lon = ''

# access coordinates of location
if country == "united states":
    city, state = input(f'please input a city and state (city, state):\n').split(',')
    geocode = requests.get(
        f'http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&limit=1&appid={api_key}')
else:
    city = input("please input a city:\n")
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







