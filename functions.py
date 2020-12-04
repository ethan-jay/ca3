'''
file containing functions referenced in ca3.py
'''
import json
import pyttsx3
from datetime import datetime
def delete_list_item(dictionary_list, list_title,schedule,isalarm=False):
    #removes a list item from its list based of title
    for item in dictionary_list:
        if item['title'] == list_title:
            if isalarm and item['content'] > datetime.now():
                try:
                    schedule.cancel(item['eventID'])
                except:
                    print("Error with cancelling scheduled event")
            dictionary_list.remove(item)
def datetime_difference_seconds(date1,date2):
    #calculate difference in seconds between dates
    timedifference = date1 - date2
    seconds = timedifference.total_seconds()
    return seconds
def alarm_time_reached(dictionary_list,schedule,alarm_title):
    #commences tts alarm
    engine = pyttsx3.init()
    engine.say(alarm_title)
    engine.runAndWait()
    load_config()
    delete_list_item(dictionary_list,alarm_title,schedule,True)
def load_config():
    #loads config file and grabs APIkeys and City name, returns them in a list of config(city,weatherAPI,newsAPIkey)
    with open('config.json', 'r') as config:
        data = json.load(config)
    weather_api_key = data['weatherAPIkey']
    news_api_key = data['newsAPIkey']
    city = data['city']
    country_code = data['countrycode']
    public_health_api_link = data['PublicHealthAPIlink']
    initconfig=[]
    initconfig.append(weather_api_key)
    initconfig.append(news_api_key)
    initconfig.append(public_health_api_link)
    initconfig.append(city)
    initconfig.append(country_code)
    return initconfig
	