import tweepy
import time
from tweepy import OAuthHandler

consumer_key ='XfZREHUUvK5QjVi47RaFeqMYu'
consumer_secret ='C9ZWeWzJmEDfAIZNtEV5ow09BmwlHvn4dca7lr4pPWiYnU6dTD'
access_token ='819536441231441920-OBCbbFcBeZ4av2tqoGdhXuqoeb7psqA'
access_secret = 'uipwPKnvXtv4pa2xxZ1zYmYty9WmKiidjNmbmBJbk6Msi'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

onoma1=raw_input("Dwse to proto onoma:")
onoma2=raw_input("Dwse to deutero onoma:")

users1 = tweepy.Cursor(api.followers, screen_name=onoma1).items()
listaf1=[]
while True:
    try:
        user1 = next(users1)
    except tweepy.TweepError:
        time.sleep(60)
        user1 = next(users1)
    except StopIteration:
        break
    listaf1.append(user1.screen_name)

users2 = tweepy.Cursor(api.followers, screen_name=onoma2).items()
listaf2=[]
while True:
    try:
        user2 = next(users2)
    except tweepy.TweepError:
        time.sleep(60)
        user2 = next(users2)
    except StopIteration:
        break
    listaf2.append(user2.screen_name)

if  list(set(listaf1).intersection(listaf2))==[]:
	print "den uparxoun koinoi followers"

else:
	newlist=[]
	newlist.extend(list(set(listaf1).intersection(listaf2)))
	print "koinoi followers:"
	for i in  newlist:
			print "@",i
			
	 

