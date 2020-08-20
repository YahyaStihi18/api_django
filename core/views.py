from django.shortcuts import render
import requests
import datetime
from django.contrib import messages
import publicip



def index(request):
    today = datetime.date.today()
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
            }
    return render(request,'core/index.html',context)



def ip(request):

    ip = requests.get('https://ipapi.co/ip/').text
    url = "http://api.ipstack.com/{}?access_key=36b65ab092455a14f25413ae9dc8e9b0"
    if request.method == 'POST':
        searchWord = request.POST.get('search','')
        try:        
            ip = searchWord
            r = requests.get(url.format(ip)).json()
            context = {
        'ip':ip,
        'continent_name':r['continent_name'],
        'country_name':r['country_name'],
        'country_flag':r['location']['country_flag'],
        'capital':r['location']['capital'],
        'languages':r['location']['languages'][0]['name'],
        'region_name':r['region_name'],
        'region_code':r['region_code'],
        'city':r['city'],
        'zip':r['zip'],
        'latitude':r['latitude'],
        'longitude':r['longitude'],
            }
            return render(request,'core/ip.html',context)
        except :
            messages.error(request, 'IP not found !!')
    ip = requests.get('https://ipapi.co/ip/').text
    r = requests.get(url.format(ip)).json()
    context = {
        'ip':ip,
        'continent_name':r['continent_name'],
        'country_name':r['country_name'],
        'country_flag':r['location']['country_flag'],
        'capital':r['location']['capital'],
        'languages':r['location']['languages'][0]['name'],
        'region_name':r['region_name'],
        'region_code':r['region_code'],
        'city':r['city'],
        'zip':r['zip'],
        'latitude':r['latitude'],
        'longitude':r['longitude'],


            }

    return render(request,'core/ip.html',context)


