import re

def generate_hashtags(post):
    # Remove special characters and split the post into words
    words = re.findall(r'\w+', post.lower())
    
    # Remove common stop words
    stop_words = {'a', 'an', 'the', 'in', 'on', 'at', 'for', 'with', 'to', 'of', 'and', 'but', 'or', 'so', 'is', 'are', 'was', 'were', 'it', 'this', 'that', 'these', 'those'}
    words = [word for word in words if word not in stop_words]
    
    # Generate hashtags
    hashtags = ['#' + word for word in words]
    
    return hashtags

# Example usage
post = "Amazing sunset at the beach today, feeling grateful #beach #sunset #grateful"
hashtags = generate_hashtags(post)
print("Generated hashtags:", " ".join(hashtags))
