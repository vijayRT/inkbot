import nltk
import os
import requests
from nltk.twitter import Query, Streamer, Twitter, TweetViewer, TweetWriter, credsfromfile
import twitter as TW
from os import listdir
from os.path import isfile, join
import json
import time


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

files = [f for f in listdir('articles')]
for f in files:
    filepath = join('articles', f)
    with open(filepath, 'r') as json_file:
        json_data = json.load(json_file)
        print(f)
        for i in range (0, 10):
            try:
                x = str(i)
                trend = json_data[x]['trend']
                tweets = client.search_tweets(keywords=trend, limit=10)
                for tweet in tweets:
                    tweet_id = tweet['id']
                    tweet_json = api.GetStatusOembed(status_id=tweet_id, align = 'center')
                    json_data[x]['tweet'] = tweet_json['html']
            except Exception as e:
                print(e)
    with open(filepath, 'w') as json_file:
        json.dump(json_data, json_file, indent = 4) 
                

