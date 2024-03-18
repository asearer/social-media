import tkinter as tk
from tkinter import ttk
import facebook
import schedule
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Facebook API credentials (replace with your own)
facebook_access_token = 'Facebook_Access_Token'

# Create a Facebook Graph API object
try:
    graph = facebook.GraphAPI(access_token=facebook_access_token)
    logging.info("Facebook authentication successful.")
except Exception as e:
    logging.error(f"Failed to authenticate with Facebook Graph API: {e}")

def post_facebook(message):
    """
    Function to post on Facebook.

    Parameters:
        message (str): The text content of the post.
    """
    try:
        graph.put_object("me", "feed", message=message)
        logging.info("Post on Facebook: %s", message)
    except facebook.GraphAPIError as e:
        logging.error("Failed to post on Facebook: %s", e)

def schedule_facebook_post():
    """
    Function to schedule a Facebook post based on user input.
    """
    message = message_entry.get()
    time_str = time_entry.get()
    hour, minute = map(int, time_str.split(':'))
    schedule.every().day.at(f"{hour:02d}:{minute:02d}").do(post_facebook, message)
    logging.info("Facebook post scheduled: %s at %s", message, time_str)
    status_label.config(text="Facebook post scheduled successfully!")

# Create GUI
root = tk.Tk()
root.title("Facebook Post Scheduler")

# Frame for input fields
input_frame = ttk.Frame(root, padding="20")
input_frame.grid(row=0, column=0, sticky="w")

# Message input field
message_label = ttk.Label(input_frame, text="Post message:")
message_label.grid(row=0, column=0, sticky="w")
message_entry = ttk.Entry(input_frame, width=50)
message_entry.grid(row=0, column=1, padx=(10, 0), sticky="w")

# Time input field
time_label = ttk.Label(input_frame, text="Scheduled time (HH:MM):")
time_label.grid(row=1, column=0, sticky="w")
time_entry = ttk.Entry(input_frame, width=10)
time_entry.grid(row=1, column=1, padx=(10, 0), sticky="w")

# Schedule button
schedule_button = ttk.Button(input_frame, text="Schedule Post", command=schedule_facebook_post)
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
