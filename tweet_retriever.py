import nltk
import os
import requests
from nltk.twitter import Query, Streamer, Twitter, TweetViewer, TweetWriter, credsfromfile
import twitter as TW
from os import listdir
from os.path import isfile, join


app_key= 'Osyy0PSrhMRpnIWxjBLzLJeKR'
app_secret= 'AYY7Qb48yl2gk4GacSmnWTrv6keikGpMAsPZaamKIRNoWYqzKI'
oauth_token= '220306570-Lk0wOlgGNaRBToOt8FIWbko1pTGvb3ZtyAfow5GN '
oauth_token_secret= 'VcNiPnSuk7LOzC2QYSJkOwgehplBmkXuzp7EwZgE69S1r'


api = TW.Api(consumer_key=app_key,
                  consumer_secret=app_secret,
                  access_token_key=oauth_token,
                  access_token_secret=oauth_token_secret)


oauth = credsfromfile()
client = Query(**oauth)
client.register(TweetViewer(limit=10))

onlyfiles = [f for f in listdir('trends')]
for  filename in onlyfiles:
    print(filename + ':\n\n')
    filepath = join('trends', filename)
    with open(filepath) as fname:
        trends = fname.readlines()
        trends = [x.strip() for x in trends]
        for trend in trends:
            print(trend + ':\n')
            tweets = client.search_tweets(keywords=trend, limit=10)
            for tweet in tweets:
                tweet_id = tweet['id']
                tweet_json = api.GetStatusOembed(status_id=tweet_id)
                print(tweet_json['html'])
                print("\n")

