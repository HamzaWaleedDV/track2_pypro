# https://api.openweathermap.org/data/2.5/weather?q=cairo&appid=40e810a12e9cd1f341cd343068894789
import requests, json

api_key = '40e810a12e9cd1f341cd343068894789'

base_url = 'https://api.openweathermap.org/data/2.5/weather?'

city_name = input('Enter city name: ')

full_url = base_url + 'q=' + city_name + '&appid=' + api_key + '&units=metric'

response = requests.get(full_url)

x = json.loads(response.text)

if x['cod'] != '404':
    y = x['main']

    ct = y['temp']
    cp = y['pressure']
    sh = y['humidity']

    z = x['weather']
    d = z[0]['description']

    print("Temp = " + str(ct)
          + "\n pressure = " +
          str(cp) +
          "\n humidity = " + 
          str(sh) +
          "\n description = " +
          str(d)
          )

else:
    print('City not found!')