import tweepy

CONSUMER_KEY ='8fqVXXylXJJ1ocO77zwVHwGoF'


CONSUMER_SECRET ='gUVOyrTtoIjkSgOM9MNOWb8vKFqQ21qxGnZG7uT4viUdnxA9yd'

ACCESS_TOKEN =' 1439425364-MwJrqDy8acP5QRI1ZzMT5vlOqbKJfPNWsdVojjy'

ACCESS_TOKEN_SECRET = '6x42q2qXMQJYjNdqXKNeeRFem5cGeqLd0vd2XOvT7Twek'

auth = tweepy.OAuthhandler(CONSUMER_KEY, CONSUMER_SECRET)

auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

twitter = tweepy.API(auth)

twiter.update_status(status = "it worked")

print("done,exiting")