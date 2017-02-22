from nltk.twitter import Query, Streamer, Twitter, TweetViewer, TweetWriter, credsfromfile

tw = Twitter()

oauth = credsfromfile()
client = Query(**oauth)
client.register(TweetViewer(limit=10))
tweets = client.search_tweets(keywords='mallya', limit=10)
tweet = next(tweets)
for tweet in tweets:
    print(tweet['text'])
    print("\n")

