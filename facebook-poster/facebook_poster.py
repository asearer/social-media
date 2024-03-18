import facebook
import schedule
import time

# Facebook API credentials 
access_token = 'Access_Token'

# Create a Facebook Graph API object
graph = facebook.GraphAPI(access_token)

def post_facebook(message):
    """
    Function to post on Facebook.

    Parameters:
        message (str): The text content of the post.
    """
    graph.put_object("me", "feed", message=message)
    print("Post on Facebook:", message)

# Schedule your posts
schedule.every().day.at("10:00").do(post_facebook, "Good morning, world!")
schedule.every().day.at("15:00").do(post_facebook, "Afternoon folks!")
schedule.every().day.at("20:00").do(post_facebook, "Good evening everyone!")

# Keep the program running
while True:
    schedule.run_pending()
    time.sleep(1)
