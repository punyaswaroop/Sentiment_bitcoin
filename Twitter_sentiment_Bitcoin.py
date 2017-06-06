# -*- coding: utf-8 -*-
"""
Created on Tue May 30 19:48:25 2017

@author: chara
"""

from textblob import TextBlob
import tweepy

consumer_key='QzOCRtkTu8UBRD4NM8b49SixV'
consumer_secret='sHxFG46TNAXFGjfpT9vxKVHJ1Yx4oZXD6hJ6qSQS8HiukwFPWk'
access_token='2493076579-PJUEldcCXQM70jglnt79vT6ZPdOSgL9SBYlxMTg'
access_token_secret='sNhvqLLLcFPUvRKhCyXMv7a77eBydWPqPVbP3lGhr0VEm'

authentication_init=tweepy.OAuthHandler(consumer_key,consumer_secret)
authentication_init.set_access_token(access_token,access_token_secret)
api=tweepy.API(authentication_init)

tweets=api.search('Bitcoin')

for tweet in tweets:
    print (tweet.text)
    text_analysis=TextBlob(tweet.text)
    print (text_analysis.sentiment)
    
