import tweepy
import time
import random
from time import sleep
import math

from credentials import *
try:
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    z = 1000

    def pooltings():
        for tweet in tweepy.Cursor(api.search, q=('#ikokazi OR #ikokazike OR #ikokaziug'), count=100,
                               result_type="recent").items(z):
            try:
                print('\nTweet by: @' + tweet.user.screen_name)
                tweet.retweet()
                print('Retweeted the tweet')
                r = random.randint(120,720)
                s = r/60
                w = round(s,1)
                if w == 10:
                    while True:
                        tweet.favorite()
                        print('Favorited & tweeted ' + tweet.user.screen_name + ' s tweet')
                    for follower in tweepy.Cursor(api.followers).items(3):
                        follower.follow()
                        print('You followed: @' + follower.screen_name)
                        a = 1
                    if(a == 1):
                        break
                else:
                    print('Sleeping for '+ str(w) + ' minute/s')
                    sleep(r)

            except tweepy.TweepError as e:
                print(e.reason)
                print("Session ended")
                u = random.randint(0,5)
                print('Restarting in ' + str(u) + ' seconds')
                sleep(u)
                continue
            # break
    pooltings()
except time.time() as x:
    print('Amsha bot' + str(x))
