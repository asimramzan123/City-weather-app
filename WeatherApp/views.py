from django.shortcuts import render
import urllib.request
import json

def weather_search_view(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' + 
            city + '&units=metric&appid=adc191f0c7e213d74e671dbe7e2dce32'
            ).read()
        # CONVERT JSON DATA INTO DICT
        listOfData = json.loads(source)

        # define data in dict you want to get
        data = {
            'country_code':str(listOfData['sys']['country']),
            'coordinate':str(listOfData['coord']['lon']) + "," + str(listOfData['coord']['lat']),
            'temp':str(listOfData['main']["temp"]) + "°C",
            'feels_like':str(listOfData['main']["feels_like"]),
            'pressure':str(listOfData['main']["pressure"]),
            'humidity':str(listOfData['main']["humidity"]),
            'main':str(listOfData["weather"][0]['main']),
            'description':str(listOfData["weather"][0]['description']),
            'icon':str(listOfData["weather"][0]['icon']),
            'wind_speed':str(listOfData["wind"]['speed']),
        }
        print(data)
    else:
        data ={}
    return render(request, 'WeatherApp/home.html', data)    


