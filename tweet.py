#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tweepy import API, OAuthHandler, TweepError #  To install tweepy: 'sudo apt-get install python-tweepy'
from time import gmtime, strftime

# enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'dS3RgnaO2UMbYSXFd3aGWdlog'  # keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'zWmGQLiV5ZYPn3cKgFx1etmVx5tZxNYYb9mbO8ZA85p2OwaPDA'  # keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '3001952026-sml60Kzd2CAshTGJlHQ6XjayzvDScKSjgMsz8uU'  # keep the quotes, replace this with your access token
ACCESS_SECRET = 'pcp4WSS9Xbgl2BeAzqMsmiOsh45SSMeQbrVUHw3iXIS1d'  # keep the quotes, replace this with your access token secret

# CONSUMER_KEY = 'smKPha7HV7DOyjplpEChF9sHm'  # keep the quotes, replace this with your consumer key
# CONSUMER_SECRET = 'taKycUV7x1TF7ny8OmVv5MUu7LfbRFVUbbXTQAonw0tmTb3pkV'  # keep the quotes, replace this with your consumer secret key
# ACCESS_KEY = '54524233-1k2JbZsaZ6nOfnmKIjA2Z1z2BXXtrSY8QerAYVfeI'  # keep the quotes, replace this with your access token
# ACCESS_SECRET = 'LmnwkviGIxvyhulvvLBSHcBkTRMbjWMXJnaaHgGrTeGQZ'  # keep the quotes, replace this with your access token secret
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)


def tweet():
    try:
        api = API(auth)
        # line = "@timvsteenbergen Met mijn account: Ding Dong at " + strftime("%l:%M %p on %d-%m-%Y")
        line = "@timvsteenbergen: Ding Dong at " + strftime("%l:%M %p on %d-%m-%Y")

        api.update_status(status=line)
        print('tried to tweet to me and succeeded. \nSent this line: ' + line)
    except TweepError as e:
        print 'Errorcode ' + str(e.message[0]['code']) + '. Meaning: ' + e.message[0]['message']
        print 'Errorcode ' + str(e.args[0][0]['code']) + '. Meaning: ' + e.args[0][0]['message']
