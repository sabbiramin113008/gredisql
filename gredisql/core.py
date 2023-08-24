# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 12 Mar 2023
email: sabbir.amin@goava.com, sabbiramin.cse11ruet@gmail.com 

"""
import json

import redis
from ariadne import load_schema_from_path, QueryType, make_executable_schema, graphql_sync, MutationType
from flask import Flask, request, jsonify

type_defs = load_schema_from_path("schema.graphql")
query = QueryType()
mutation = MutationType()

REDIS_host = 'localhost'
REDIS_port = 6379
REDIS_db = 0
REDIS_decode_response = True

rr = redis.StrictRedis(host=REDIS_host,
                       port=REDIS_port,
                       db=REDIS_db,
                       decode_responses=REDIS_decode_response)
