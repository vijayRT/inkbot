#tweepy1.py - To test trend obtaining

import sys
sys.path.append('/home/vijay/.local/lib/python2.7/site-packages')

import tweepy
import woeid
import yweather
import time
import os

#Configure Tweepy API
t0 = time.time()

consumer_key = 'Osyy0PSrhMRpnIWxjBLzLJeKR'
consumer_secret = 'AYY7Qb48yl2gk4GacSmnWTrv6keikGpMAsPZaamKIRNoWYqzKI'
access_token = '220306570-Lk0wOlgGNaRBToOt8FIWbko1pTGvb3ZtyAfow5GN'
access_token_secret = 'VcNiPnSuk7LOzC2QYSJkOwgehplBmkXuzp7EwZgE69S1r'
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
tweapi = tweepy.API(auth)


#Configure Yahoo WOEID API

def get_trends(cou):

    client = yweather.Client()
    filename = cou
    filepath = os.path.join('trends', filename)
    thefile = open(filepath, 'w')
 
    place_woeid = client.fetch_woeid(cou)
    trends1 = tweapi.trends_place(place_woeid,exclude='hashtags')
    
    data = trends1[0]
    trends = data['trends']
    for trend in trends[:10]:
        thefile.write("%s\n" % trend['name'])
        

        
country_list = ['USA', 'UK', 'India', 'Canada', 'Australia']
for country in country_list:
    get_trends(country)
    print(country)
    print("\n")
    
t1 = time.time()
print(t1 - t0)
