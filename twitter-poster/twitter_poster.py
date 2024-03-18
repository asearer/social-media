import tkinter as tk
from tkinter import ttk
import tweepy
import schedule
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Twitter API credentials (replace with your own)
twitter_consumer_key = 'Your_Consumer_Key'
twitter_consumer_secret = 'Your_Consumer_Secret'
twitter_access_token = 'Your_Access_Token'
twitter_access_token_secret = 'Your_Access_Token_Secret'

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

def post_tweet(message, media=None):
    """
    Function to post a tweet.

    Parameters:
        message (str): The text content of the tweet.
        media (str): Path to media file (image, video) to be attached to the tweet.
    """
    try:
        if media:
            twitter_api.update_with_media(filename=media, status=message)
        else:
            twitter_api.update_status(message)
        logging.info("Tweet posted on Twitter: %s", message)
    except tweepy.TweepError as e:
        logging.error("Failed to post tweet on Twitter: %s", e)

def schedule_tweet():
    """
    Function to schedule a tweet based on user input.
    """
    message = message_entry.get()
    time_str = time_entry.get()
    hour, minute = map(int, time_str.split(':'))
    schedule.every().day.at(f"{hour:02d}:{minute:02d}").do(post_tweet, message)
    logging.info("Tweet scheduled: %s at %s", message, time_str)
    status_label.config(text="Tweet scheduled successfully!")

# Create GUI
root = tk.Tk()
root.title("Twitter Post Scheduler")

# Frame for input fields
input_frame = ttk.Frame(root, padding="20")
input_frame.grid(row=0, column=0, sticky="w")

# Message input field
message_label = ttk.Label(input_frame, text="Tweet message:")
message_label.grid(row=0, column=0, sticky="w")
message_entry = ttk.Entry(input_frame, width=50)
message_entry.grid(row=0, column=1, padx=(10, 0), sticky="w")

# Time input field
time_label = ttk.Label(input_frame, text="Scheduled time (HH:MM):")
time_label.grid(row=1, column=0, sticky="w")
time_entry = ttk.Entry(input_frame, width=10)
time_entry.grid(row=1, column=1, padx=(10, 0), sticky="w")

# Schedule button
schedule_button = ttk.Button(input_frame, text="Schedule Tweet", command=schedule_tweet)
schedule_button.grid(row=2, column=0, columnspan=2, pady=(10, 0))

# Status label
status_label = ttk.Label(root, text="")
status_label.grid(row=1, column=0, padx=20, sticky="w")

# Start GUI event loop
root.mainloop()

# Keep the program running
while True:
    schedule.run_pending()
    time.sleep(1)
