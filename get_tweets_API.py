import tweepy
from tweepy import Client

client = Client(bearer_token='XXXXXXXXXXXXXXX')

def get_tweets(query):
    tweets = []
    
    try:
        for tweet in tweepy.Paginator(client.search_recent_tweets, query=query,
                              tweet_fields=['context_annotations', 'created_at'], max_results=100).flatten(limit=1000):
            tweets.append(tweet.text)
        return tweets
    
    except: 
        print("Error calling Twitter API!")
            
# get_tweets('Hey!')
