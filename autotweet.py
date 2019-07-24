#!/usr/bin/python3

import tweepy, m_config
from random import randint
from time import sleep

auth = tweepy.OAuthHandler(m_config.CONSUMER_KEY, m_config.CONSUMER_SECRET)
auth.set_access_token(m_config.ACCESS_TOKEN, m_config.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

bef = 0
aft = 0

while True:
    while bef == aft:
        aft = randint(0, len(m_config.array) - 1)
    try:
        api.update_status(m_config.array[aft])
        print("bef : " + str(bef) + ", aft : " + str(aft))
        bef = aft
        delay = randint(20000, 30000)
        print("delay : " + str(delay))
        sleep(delay)
    except:
        continue
