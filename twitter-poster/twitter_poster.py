import tweepy
import schedule
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Twitter API credentials 
twitter_consumer_key = 'Consumer_Key'
twitter_consumer_secret = 'Consumer_Secret'
twitter_access_token = 'Access_Token'
twitter_access_token_secret = 'Access_Token_Secret'

# Authenticate to Twitter
try:
    twitter_auth = tweepy.OAuth1UserHandler(twitter_consumer_key, twitter_consumer_secret, twitter_access_token, twitter_access_token_secret)
    twitter_api = tweepy.API(twitter_auth)
    logging.info("Twitter authentication successful.")
except Exception as e:
    logging.error(f"Failed to authenticate with Twitter API: {e}")

# Define message templates
message_templates = {
    "morning": "Good morning, world! 🌅",
    "afternoon": "Afternoon folks! 🌞",
    "evening": "Good evening everyone! 🌙"
}

def post_tweet(message):
    """
    Function to post a tweet.

    Parameters:
        message (str): The text content of the tweet.
    """
    try:
        twitter_api.update_status(message)
        logging.info("Tweet posted on Twitter: %s", message)
    except tweepy.TweepError as e:
        logging.error("Failed to post tweet on Twitter: %s", e)

# Schedule your tweets
schedule.every().day.at("10:00").do(post_tweet, message_templates["morning"])
schedule.every().day.at("15:00").do(post_tweet, message_templates["afternoon"])
schedule.every().day.at("20:00").do(post_tweet, message_templates["evening"])

# Keep the program running
while True:
    schedule.run_pending()
    time.sleep(1)
