from googleapiclient.discovery import build

 
api_key = 'AIzaSyCb5VnUNMp9XEKB0T5FRErO0xl_Xr7xIS4'
youtube = build('youtube','v3',developerKey=api_key)
r = youtube.search().list(q='Algerian viral video',maxResults=10,part='snippet',type='video')
res = r.execute()
x=  len(res['items'])
print(x)

#https://www.youtube.com/watch?v=123123asdsad12