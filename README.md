# Twitter APIs

The Twitter API is a set of programmatic endpoints that can be used to understand or build the conversation on Twitter. This API allows you to find and retrieve, engage with, or create a variety of different resources. 

## Prerequisite

- In order to work with the Twitter API, we need to have a developer account and our API keys and tokens to connect to the API.

- In order to work with Tweepy, make sure you have Python installed on your machine. Then, in the terminal run:
      ### pip install tweepy

- You will first need to import the tweepy library, then you will need to initialize the client by passing it your bearer token. Once you have the client initialized, you will be ready to start using the various functions in this library.

## APIs

### Search Tweets:
- In the get_tweets Python file added, after replacing the bearer token and putting a desired search query, we get the text of various tweets aligned to that query. 
- For more than 100 Tweets, we will have to use the paginator and specify the limit i.e. the total number of Tweets required.
- Try and except method is used to give error if the Twitter is not responding. 

### Get Tweets:
- In the get_tweets Python file added, after replacing the bearer token and putting a user id, we get the tweets of that user. 
- Try and except method is used to give error if the Twitter is not responding. 

## Botometer
Botometer runs analysis on whether the user is likely a bot or a human. The threshold score is anything less then 0.5 Botometer predicts the user is most likely controlled by human.

- Run Botometer, using Twitter’s Api, on a few users.
- First I authenticated Botometer with Twitter’s API credentials similiar to Tweepy. I also needed a rapidapi key for Botometer 
