# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 30 Aug 2023
email: sabbir.amin@goava.com, sabbiramin.cse11ruet@gmail.com

"""

import redis

REDIS_host = 'localhost'
REDIS_port = 6379
REDIS_db = 0
REDIS_decode_response = True

rr = redis.StrictRedis(host=REDIS_host,
                       port=REDIS_port,
                       db=REDIS_db,
                       decode_responses=REDIS_decode_response)

if __name__ == '__main__':
    # print(rr.info())
    print(rr.mset({'hello': 'world'}))
