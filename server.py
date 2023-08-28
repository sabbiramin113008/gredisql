# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 29 Aug 2023
email: sabbir.amin@goava.com, sabbiramin.cse11ruet@gmail.com

"""
import redis
from ariadne import QueryType, gql, make_executable_schema
from ariadne import load_schema_from_path
from ariadne.asgi import GraphQL
import json
type_defs = gql("""
    type Query {
        hello: String!
    }
""")

type_defs = load_schema_from_path("schema.graphql")

# Create type instance for Query type defined in our schema...
query = QueryType()

# Redis specific stuffs
REDIS_host = 'localhost'
REDIS_port = 6379
REDIS_db = 0
REDIS_decode_response = True

rr = redis.StrictRedis(host=REDIS_host,
                       port=REDIS_port,
                       db=REDIS_db,
                       decode_responses=REDIS_decode_response)


@query.field("set")
def resolve_set(_, info, name, value, ex=None):
    status = rr.set(name, json.dumps(value), ex)
    response = {
        'status': status
    }
    return response


@query.field("get")
def resolve_set(_, info, name):
    value = rr.get(name)
    response = {
        'value': json.loads(value) if value else None,
        'status': True if value else False

    }
    return response


schema = make_executable_schema(type_defs, query)
app = GraphQL(schema, debug=True)
