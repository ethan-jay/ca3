'''
functions that deal with news data
'''
import requests
def news_api(country_code,news_api_key):
    #completes url and requests the data from it
    #example url : 'http://newsapi.org/v2/top-headlines?country=us&apiKey=752980a707ed43b799590cf737118976'
    base_url = "http://newsapi.org/v2/top-headlines?"
    complete_url = base_url + 'country=' + country_code + '&apiKey=' + news_api_key
    response = requests.get(complete_url)
    return response
def process_news_api(dictionary_api,notification_dictionary):
    #processes info gathered to be put into display dictionarys , 3 news articles
    for number in range(3):
        article_title = dictionary_api.json()['articles'][number]['title']
        article_description = dictionary_api.json()['articles'][number]['description']
        notification_dictionary.append({'title':article_title,'content':article_description})
		