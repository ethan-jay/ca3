'''
functions that deal with weather data
'''
from datetime import datetime
import requests
def weather_api(city,weather_api_key):
    #api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key} is the url format needed
    #completes url and requests the data from it
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + 'q=' + city + '&appid=' + weather_api_key
    response = requests.get(complete_url)
    return response
def process_weather_api(dictionary_api,notification_dictionary):
    #processes info gathered to be put into display dictionarys
    weather_desc = dictionary_api.json()['weather'][0]['description']
    temperature = str(dictionary_api.json()['main']['temp'])
    feels_like = str(dictionary_api.json()['main']['feels_like'])
    content_str = weather_desc + " " + temperature + " "  + feels_like
    notification_dictionary.append({'title':"Current Weather at " + str(datetime.now()),'content':content_str})
