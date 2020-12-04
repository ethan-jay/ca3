'''
Program main, schedules events and refers to functions elsewhere to complete nessesary actions
'''
import time
import sched
import logging
from datetime import datetime
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from covid_api import covid19_api
from covid_api import process_covid19_api
from news_api import news_api
from news_api import process_news_api
from weather_api import weather_api
from weather_api import process_weather_api
from functions import delete_list_item
from functions import datetime_difference_seconds
from functions import alarm_time_reached
from functions import load_config
logging.basicConfig(filename='sys.log', encoding='utf-8')
s = sched.scheduler(time.time, time.sleep)
app = Flask(__name__)
notifications = []
alarms = []
@app.route('/')
def index_redirect():
    return redirect('/index')
@app.route('/index')
def schedule_event():
    s.run(blocking=False)
    alarm_time = request.args.get("alarm")
    config = load_config()
    if alarm_time:
        #convert alarm_time to a delay
        alarm_title = request.args.get("two")
        current_time = datetime.now()
        alarm_time_obj = datetime.strptime(alarm_time, "%Y-%m-%dT%H:%M")
        delay = datetime_difference_seconds(alarm_time_obj,current_time)
        repeat = False
        for item in alarms:
            if item['title'] == alarm_title:
                repeat = True
        if delay > 0 and not repeat:
            scheduled_event = s.enter(int(delay), 1, alarm_time_reached, argument=(alarms,s,request.args.get("two"),) )
            alarms.append({'title':alarm_title,'content':alarm_time_obj,'eventID':scheduled_event})
    if request.args.get("notif"):
        #removes notification when x is clicked
        delete_list_item(notifications,request.args.get("notif"),s,False)
    if request.args.get("alarm_item"):
        #cancels an alarm when x is clicked
        delete_list_item(alarms,request.args.get("alarm_item"),s,True)
    if request.args.get("news"):
        #runs news update
        news_dictionary = news_api(config[4],config[1]) #config[3] is country code, config[2] is newsapikey
        process_news_api(news_dictionary,notifications)
        covid_dictionary = covid19_api(config[2])
        process_covid19_api(covid_dictionary,notifications)
    if request.args.get("weather"):
        #runs weather update
        weather_dictionary = weather_api(config[3],config[0]) #config[0] is city, config [1] is weatherapikey
        process_weather_api(weather_dictionary,notifications)
    return  render_template('index.html', alarms = alarms, notifications=notifications,image='clock.jpeg')
if __name__ == '__main__':
    app.run()
