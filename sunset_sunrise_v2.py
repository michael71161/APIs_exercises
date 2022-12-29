#Here we going to modify our request. we will add aditional param
#to get 24h format time with date and time . we will take the time 
#using the split() method 

import requests
from datetime import datetime

#beer sheva 
MY_LAT = 31.243870
MY_LONG = 34.793991


parameters = {
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted":0,
}

#request to sever 
response = requests.get(" https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()   #now data contain all the long response 
print(data)
sunrise = data["results"]["sunrise"] #access to dict inside a dict we want to get the values of the keys result, sunrise
sunset = data["results"]["sunset"] #same with sunset as key and value, we getting the value
print (sunrise)
#print(sunset)
time_now = datetime.now()
#print(time_now)
sunrise_24h = sunrise.split("T")[1] #we split the string on the t than 
#we select the item in the list located on place 1 (list stars with 0)
print(sunrise_24h)