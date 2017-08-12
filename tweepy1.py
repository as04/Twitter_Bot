import tweepy
import time
from time import sleep
con_key=''
con_secret=''
access_token=''
access_token_secret=''
auth=tweepy.OAuthHandler(con_key,con_secret)
auth.set_access_token(access_token,access_token_secret)
auth.secure=True
api=tweepy.API(auth)
#print(str(api.get_user(screen_name='@crazyyButter ')))

handle=input("Enter User handle ")
user=api.get_user(handle)

sleeptime = 4
pages = tweepy.Cursor(api.followers, screen_name=handle).pages()

print("Followers of "+handle)

while True:
    try:
        page = next(pages)
        time.sleep(sleeptime)
    except tweepy.TweepError: #taking extra care of the "rate limit exceeded"
        time.sleep(60*15) 
        page = next(pages)
    except StopIteration:
        break
    for user in page:
    	#print(user.id_str)
    	print(user.screen_name)
    	#print(user.followers_count)
#sleeptime = 4
pages = tweepy.Cursor(api.friends, screen_name=handle).pages()

print("Followings of "+handle)


while True:
    try:
        page = next(pages)
        time.sleep(sleeptime)
    except tweepy.TweepError: #taking extra care of the "rate limit exceeded"
        time.sleep(60*15) 
        page = next(pages)
    except StopIteration:
        break
    for user in page:
    	#print(user.id_str)
    	print(user.screen_name)
    	#print(user.followers_count)
print("Favorite Tweets for #IOT")
pages = tweepy.Cursor(api.search, q='#IOT').pages()

c=0
while True:
    try:
        page = next(pages)
        time.sleep(sleeptime)
    except tweepy.TweepError: #taking extra care of the "rate limit exceeded"
        time.sleep(60*15) 
        page = next(pages)
    except StopIteration:
        break
    for tweet in page:
    	try:
    		if(tweet.favorited==False):
    			tweet.favorite()
    			c=c+1
    	except tweepy.TweepError as e:
    		print(e.reason)
    		sleep(2)
    		continue
    	except StopIteration:
    		break
print(c)
print("Tweetes favorited for #IOT")

print("Favorite tweets for @boltiot")

new_tweets = api.user_timeline(screen_name = 'boltiot')
c=0
for tweet in new_tweets:
	try:
		if(tweet.favorited==False):
			tweet.favorite()
	except tweepy.TweepError as e:
		print(e.reason)
		sleep(2)
		continue
	except StopIteration:
		break
	