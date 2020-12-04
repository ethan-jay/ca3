'''
functions that deal with covid 19 data
'''
import requests
def covid19_api(link):
    #presents covid-19 information in users notification list based on link created https://coronavirus.data.gov.uk/details/download
    complete_url = link
    response = requests.get(complete_url)
    return response
def process_covid19_api(dictionary_api,notification_dictionary):
    #processes covid 19 data for display
    covid_deaths28 = dictionary_api.json()['body'][0]["cumDeaths28DaysByPublishDate"]
    covid_cases28 = dictionary_api.json()['body'][0]["cumCasesByPublishDate"]
    notification_dictionary.append({'title':"Covid-19 deaths in the last 28 days",'content':covid_deaths28})
    notification_dictionary.append({'title':"Covid-19 cases last 28 days",'content':covid_cases28})
