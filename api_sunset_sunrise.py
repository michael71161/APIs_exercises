# we are going to use sunset, sunrise API , we going to provide lang and alt 
#for lat and long  we will use my beloved hometown Beer-Sheva 
#we are using built in requests library (import requests) for 
#our requests to our server (API)
 
import requests

#beer sheva 
MY_LAT = 31.243870
MY_LONG = 34.793991


parameters = {
    "lat":MY_LAT,
    "lng":MY_LONG,
}

#request to sever 
response = requests.get(" https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()   #now data contain all the long response 
print(data)
sunrise = data["results"]["sunrise"] #access to dict inside a dict we want to get the values of the keys result, sunrise
sunset = data["results"]["sunset"] #same with sunset as key and value, we getting the value
print (sunrise)
print(sunset)






