#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys
from tweepy import OAuthHandler
from time import gmtime, strftime

# enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'dS3RgnaO2UMbYSXFd3aGWdlog'  # keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'zWmGQLiV5ZYPn3cKgFx1etmVx5tZxNYYb9mbO8ZA85p2OwaPDA'  # keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '3001952026-sml60Kzd2CAshTGJlHQ6XjayzvDScKSjgMsz8uU'  # keep the quotes, replace this with your access token
ACCESS_SECRET = 'pcp4WSS9Xbgl2BeAzqMsmiOsh45SSMeQbrVUHw3iXIS1d'  # keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

try:
    api = tweepy.API(auth)
    line = "@in06khattab Ding Dong at " + strftime("%l:%M %p on %d-%m-%Y")

    api.update_status(status=line)
except tweepy.TweepError as e:
    print e.message[0]['code']  # prints 34
    print e.args[0][0]['code']  # prints 34
