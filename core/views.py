from django.shortcuts import render
import requests
import datetime


def index(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=7d3e88675b678961df9ba90435e7a5f6'
    city = 'jijel'
    r = requests.get(url.format(city)).json()
    today = datetime.date.today()
    weather = {
        
        'city':city,
        'temperature':r['main']['temp'],
        'wind':r['wind']['speed'],
        'wind_deg':r['wind']['deg'],
        'description':r['weather'][0]['description'],
        'icon':r['weather'][0]['icon'],
    } 
    context = {
        'weather':weather,
        'today':today,
    }
    return render(request,'core/index.html',context)