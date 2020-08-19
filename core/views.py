from django.shortcuts import render
import requests
import datetime
from django.contrib import messages
from ipware import get_client_ip



def index(request):
    today = datetime.date.today()

    ip = request.META.get("REMOTE_ADDR")
    urlip = 'http://api.ipstack.com/{}?access_key=36b65ab092455a14f25413ae9dc8e9b0'
    r = requests.get(urlip.format(ip)).json()
    ip_info = {
        'ip':ip,
        'country_code':country_code,
    }

    print(ip)
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=7d3e88675b678961df9ba90435e7a5f6'
    
    if request.method == 'POST':
        searchWord = request.POST.get('search','')
        try:        
            city = searchWord

            r = requests.get(url.format(city)).json()
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
        'ip_info':ip_info,
            }
            return render(request,'core/index.html',context)
        except :
            messages.error(request, 'city not found !!')

    city = 'jijel'
    r = requests.get(url.format(city)).json()
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
        'ip_info':ip_info,
            }
    return render(request,'core/index.html',context)
