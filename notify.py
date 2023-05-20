import plyer
from plyer import notification
import requests
import datetime
import time

covidStats=None
try:
    covidStats=requests.get("https://corona-rest-api.herokuapp.com/Api/uganda")
except:
    print('Nigga u lack  data')
    
if (covidStats != None):
    jsonData = covidStats.json()['Success'] 
    
while True:
    notification.notify(
        title='COVID19 Stats on{}'.format(datetime.date.today()),
        message = "Total cases : {totalcases}\nToday cases : {todaycases}\nToday deaths : {todaydeaths}\nTotal active : {active}".format(  
                        totalcases = jsonData['cases'],  
                        todaycases = jsonData['todayCases'],  
                        todaydeaths = jsonData['todayDeaths'],  
                        active = jsonData["active"]),  
        app_icon='covidProtection.png',
        timeout=3
    )
    time.sleep(60*60*12)