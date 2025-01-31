import requests
api_key = open('api_key.txt', 'r').read()
country = 'US'
state = input('Please input a state:\n')
city = input('Please input a city:\n')
limit = 1
lat = ''
lon = ''


r_latlong = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&limit={limit}&appid={api_key}')

if r_latlong.status_code == 200:
    print(r_latlong.text)
    data = r_latlong.json()
    lat = data[0]['lat']
    lon = data[0]['lon']

r_weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}')

print(lat)
print(lon)
print(r_weather)

if r_weather.status_code == 200:
    print(r_weather.text)
    data1 = r_weather.json()
    temp = data1['main']['temp']

fahr_convert = (temp - 273.15) * (9/5) + 32
print(fahr_convert)





