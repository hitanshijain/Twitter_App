import tweepy
from tweepy import Client

client = Client(bearer_token='XXXXXXXXXXXXXXX')

def search_tweets(query):
    tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=100)
    for tweet in tweets.data:
        print(tweet.text)
        if len(tweet.context_annotations) > 0:
            print(tweet.context_annotations)
            
# Replace with your own search query
search_tweets('Hey!')
