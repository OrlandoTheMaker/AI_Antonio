import tweepy
import time
import os

def cls():
    os.system("clear")


api = input(" Enter Your Api: ")
cls()
secret = input("Enter Api Secret: ")
cls()
access_token = input("Enter Your Access Token: ")
cls()
access_t_secret = input("Enter Your Access_Token_Secret: ")
cls()

auth = tweepy.OAuthHandler(api, secret)
auth.set_access_token(access_token, access_t_secret)

# Create the API object
api = tweepy.API(auth)


# Tweet a message
def tweet_message(message):
    api.update_status(message)

# Like mentions


#def like_mentions():
##    mentions = api.mentions_timeline()

 #   for mention in mentions:
 #       if mention.user.screen_name != 'Orlando The Maker':
 #           api.create_favorite(mention.id)


while True:
    tweet_message("Hello World!")
    #like_mentions()  # Like mentions

    # Wait for 1 minute before running again
    time.sleep(60)

