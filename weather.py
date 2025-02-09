import requests
from tkinter import *
from tkinter import ttk

degree_sign = u'\N{DEGREE SIGN}'

api_key = open('api_key.txt', 'r').read()

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

# TO-DO:
# Account for capitalization
# Account for invalid characters
class InputCollector:
	def __init__(self, entry):
		self.inputs = []
		self.entry = entry.get()
		self.country = ""
		self.city = ""
		self.state = ""
		self.weather_data = None
	
	def format_inputs(self):
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
		
		for data in self.inputs:
			if len(self.inputs) == 3:
				self.country = self.inputs[2]
				self.state = self.inputs[1]
				self.city = self.inputs[0]
			elif len(self.inputs) == 2:
				self.country = self.inputs[1]
				self.city = self.inputs[0]
			else:
				print("Invalid location")

	def get_inputs(self):
		return self.inputs
	
	def format_data(self):
		if self.state != "":	
			geocode = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={self.city},{self.state},{self.country}&limit=1&appid={api_key}')
		else:
			geocode = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={self.city},{self.country}&limit=1&appid={api_key}')
		
		if geocode.status_code == requests.codes.ok:
			location = geocode.json()
			lat = location[0]['lat']
			lon = location[0]['lon']
		
		weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}')
		self.weather_data = weather.json()

	def get_weather_data(self):
		return self.weather_data
		
class WeatherInfo:
	def __init__(self, weather_data):
		self.weather_data = weather_data
	
	def get_temp(self):
		temp_dict = self.weather_data["main"]
		main_temp = temp_dict["temp"]
		fahrenheit = int((main_temp - 273.15) * (9/5) + 32)
		return fahrenheit

# temperature label
temp_label = ttk.Label(content, text="Temperature: ")
temp_label.grid(column=5, row=10)
	
root.mainloop()

user_loc = InputCollector(location)
user_loc.format_inputs()
user_loc.format_data()
weather_data = user_loc.get_weather_data()

# weather info object
weather_stuff = WeatherInfo(weather_data)
one_temp = weather_stuff.get_temp()
temp = f'Temperature: {one_temp}{degree_sign}F'
print(temp)

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

print(weather.text)

# access weather data
if weather.status_code == requests.codes.ok:
    data = weather.json()
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]

print(fahr_convert)







