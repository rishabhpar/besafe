import re
import io
import csv
import tweepy
from tweepy import OAuthHandler

consumer_key = '2XFmdLC5dtjfXHkQoRNx5YOxP'
consumer_secret = 'WZO1Y4DUrXStsFPCORLZQy6VTqBMPPMcM7ZX37gyfX5tvKFATu'

access_token = '717047673711239169-PRkvMJn8gzn6yAnFfWj2jFlB3lQK4S4'
access_token_secret = 'rqTN60hRqKC7NtzPNXAmQ3H1oPqcfzdrThTj4YY77Uzq1'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

indicativeWords = ["Assault", "Kidnapping", "Theft", "Arson", "Robbery", "Burglary", "Bombing", "Murder",
                     "Manslaughter", "Crime", "Rape", "Narcotic", "Hostage", "Homicide", "Harrasment", "Larceny", "Fire", "Crash"]
target = io.open("mytweets.txt", 'w', encoding='utf-8')

def get_tweets(query, count):

    # empty list to store parsed tweets
    tweets = []
    # call twitter api to fetch tweets
    q=str(query)
    fetched_tweets = api.search(q, count = 100)
    # parsing tweets one by one
    print(len(fetched_tweets))

    for tweet in fetched_tweets:

        # empty dictionary to store required params of a tweet
        parsed_tweet = {}
        # saving text of tweet
        parsed_tweet['text'] = tweet.text
        if "http" not in tweet.text:
            line = re.sub("[^A-Za-z]", " ", tweet.text)
            target.write(line+"\n")
    return tweets

    # creating object of TwitterClient Class
    # calling function to get tweets
for word in indicativeWords:
     tweets = get_tweets(query=word, count = 100)


# tweets = []
# i = 0

# for s_name in newsSources:
#      #public_tweets = api.home_timeline()
#      tweets[i] = api.user_timeline(screen_name=s_name,
#                               # 200 is the maximum allowed count
#                               count=2000,
#                               include_rts = False,
#                               # Necessary to keep full_text
#                               # otherwise only the first 140 words are extracted
#                               tweet_mode = 'extended'
#                               )

#      for info in tweets[i][:5]:
#           print("ID: {}".format(info.id))
#           print(info.created_at)
#           print(info.full_text)
#           print("\n")
     
#      i += 1
#      # search = api.search(q="KVUE", count = 10)

#      # #trends = api.trends_place()

#      # print("Search: " + str(search))
#      # print(str(type(search)))

#      # for tweet in search:
#      #      print(type(tweet.text))
#      #      print(tweet.text)