# -*- coding: utf-8 -*-
#import redis
import botHandler as hBot
import os

# If you use redis, install this add-on https://elements.heroku.com/addons/heroku-redis
#r = redis.from_url(os.environ.get("REDIS_URL"))

#       Your bot code below

def main():
    hBot.startBot()

if __name__ == '__main__':
    main()