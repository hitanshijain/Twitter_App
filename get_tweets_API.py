import tweepy
client = tweepy.Client(bearer_token='REPLACE_ME')

def get_users():
    
    tweets = client.get_users_tweets(id=id, tweet_fields=['context_annotations','created_at','geo'])
    
    for tweet in tweets.data:
        print(tweet)
    
get_tweets('2244994945')
