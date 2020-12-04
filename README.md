# ca3
ECM1400 coursework
Author Names - Ethan Slocock (python) & Matt Collinson (html)

This is an open source "smart alarm clock" coded in python with links to an html template. This program allows users to add alarm clocks, which will play with text to speech functionality of the users label. 
Please not this will not allow users to create alarms of the same name, and will not allow users to create alarms in the past. To gather notifications, a few API's are used. I have removed my API keys, and they must be replaced in the 
config file. These will be listed below. Also note that there are several python modules that must be installed before this will function. Please run "pip install [name]" for each listed below.

API's
Openweathermap API (https://openweathermap.org)
News API(https://newsapi.org/)
UK Public Health Covid-19 API (https://coronavirus.data.gov.uk/details/download)
Note: The public health link currently stored is for Exeter. Please download a new location of the link above if you want to change location and insert into the config file. 

Modules
Flask
pyttsx3
requests-html
logging
datetime
schedule

File explanations-
CA3(FOLDER)
README.txt - Text file to explain to a user downloading the software the prerequistits and a description of the software.
ca3.py - Main file. This should be the script ran when a user wants to launch the app. Contains links to the html template.
functions.py - Contains any functions that assist with ca3.py but do not directly interact with API's.
news_api.py - Contains all functions that reference or handle data from the news api.
covid_api.py - Contains all functions that reference or handle data from the public health covid-19 api.
weather_api.py - Contains all functions that reference or handle data from the weather api.
config.json - Configuration file for easily changable aspects of the program.
	STATIC(FOLDER)
		IMAGES(FOLDER)
			clock.jpeg - clock image 
	TEMPLATES(FOLDER)
		index.html - html layout created by Matt Collinson


LICENSE:
THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, 
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR 
PERFORMANCE OF THIS SOFTWARE.



