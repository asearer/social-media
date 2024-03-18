import tweepy
import schedule
import time

# Twitter API credentials 
consumer_key = 'Consumer_Key'
consumer_secret = 'Consumer_Secret'
access_token = 'Access_Token'
access_token_secret = 'Access_Token_Secret'

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

def post_tweet(message):
    """
    Function to post a tweet.

    Parameters:
        message (str): The text content of the tweet.
    """
    api.update_status(message)
    print("Tweet posted:", message)

# Schedule your tweets
schedule.every().day.at("10:00").do(post_tweet, "Good morning, world!")
schedule.every().day.at("15:00").do(post_tweet, "Afternoon folks!")
schedule.every().day.at("20:00").do(post_tweet, "Good evening everyone!")

# Keep the program running
while True:
    schedule.run_pending()
    time.sleep(1)
