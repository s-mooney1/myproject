CONSUMER_KEY =''

CONSUMER_SECRET =''

ACCESS_TOKEN =''

ACCESS-TOKEN_SECRET = ''

auth = tweepy.OAuthhandler(CONSUMER_KEY, CONSUMER_SECRET)

auth.set_access_token(ACCESS-TOKEN, ACCESS_TOKEN_SECRET)

twitter = tweepy.API(auth)

twitter.update_status(status = "hello world")

print("done, exiting")