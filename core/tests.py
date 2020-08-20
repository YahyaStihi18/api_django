import requests



url = ('http://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=c9e0bed47e6b44dca5a613fc39accd7d')
r = requests.get(url).json()
article1 = {
    
    'title':r['articles'][0]['title'],
    'description':r['articles'][0]['description'],
    'url':r['articles'][0]['url'],
    'urlToImage':r['articles'][0]['urlToImage'],
    'publishedAt':r['articles'][0]['publishedAt'],
    'author':r['articles'][0]['author'],
}



context = {
    'article1':article1
}

print (context)