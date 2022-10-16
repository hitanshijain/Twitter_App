# Twitter APIs

The Twitter API is a set of programmatic endpoints that can be used to understand or build the conversation on Twitter. This API allows you to find and retrieve, engage with, or create a variety of different resources. 

## Product - Finance and Stock Monitoring
The stock market can be volatile and often fluctuates drastically in a short amount of time. However, some of the variables that affect the stock market can be considered before investing. For example, when deciding between investing in two companies like Amazon and Walmart, the sentiments received from the company about their latest products are evaluated. This will indicate which company is performing better in the current market and the decision can be made accordingly.

## User Stories

- As a user, if I am looking to invest in the automobile industry and confused about choosing between company X and company Y, I can look at the sentiments received from the company for their latest products. It will help me to find the one that is performing better in the market. 
- As a company manager, I want to know the reviews of my latest product and make improvements according to them. 

## Prerequisite

- In order to work with the Twitter API, we need to have a developer account and our API keys and tokens to connect to the API.

- In order to work with Tweepy, make sure you have Python installed on your machine. Then, in the terminal run:

      pip install tweepy
      import tweety

- You will first need to import the tweepy library, then you will need to initialize the client by passing it your bearer token. Once you have the client initialized, you will be ready to start using the various functions in this library.

      from tweety import Client

## APIs

### Search Tweets:
- In the search_tweets Python file added, after replacing the bearer token and putting a desired search query, we get the text of various tweets aligned to that query. 
- Using the below command, gives the tweet fields including the time at which it was created. We can give the value of max_results according to our required number of tweets. 

      tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=100)

- If you need more than 100 Tweets, you will have to use the paginator and specify the limit i.e. the total number of Tweets that you want.

      for tweet in tweepy.Paginator(client.search_recent_tweets, query=query,
                              tweet_fields=['context_annotations', 'created_at'], max_results=100).flatten(limit=1000):
            print(tweet)
            
- Try and except method is used to give error if the Twitter is not responding. 

### Get Tweets:
- In the get_tweets Python file added, after replacing the bearer token and putting a user id, we get the tweets of that user using the command:

      tweets = client.get_users_tweets(id=id, tweet_fields=['context_annotations','created_at','geo'])
      
- Try and except method is used to give error if the Twitter is not responding. 

## Botometer

- Run in the terminal:
      
      pip install botometer
      import botometer

- Run Botometer, using Twitter’s Api, on a few users.
- First I authenticated Botometer with Twitter’s API credentials similiar to Tweepy. I also needed a rapidapi key for Botometer.
- When I passed the username of a user, I got the details using the following command:

      botometer.check_account(username)
