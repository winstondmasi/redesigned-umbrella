from dotenv import load_dotenv
import tweepy
import os

load_dotenv()
consumer_key = os.environ.get("TWITTER_CONSUMER_KEY")
consumer_secret = os.environ.get("TWITTER_CONSUMER_SECRET")
access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
access_token_secret = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

# Twitter API credentials from environment variables
bearer_token = os.environ.get("TWITTER_BEARER_TOKEN")

# Initialize the tweepy client with your bearer token
client = tweepy.Client(bearer_token)

def get_tweets(username, count=10):
    # Build the query string to search for tweets from the user, excluding retweets
    query = f'from:{username} -is:retweet'

    try:
        # Fetch tweets using the query
        response = client.search_recent_tweets(query=query, max_results=count)
        
        # Check if the response includes data
        if response.data:
            # Extract the text of each tweet
            return [tweet.text for tweet in response.data]
        else:
            # No tweets were found
            return []
    except tweepy.TweepyException as e:
        # An error occurred, such as a rate limit error, print the message
        print(f"An error occurred: {e}")
        return []