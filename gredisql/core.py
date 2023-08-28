# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 12 Mar 2023
email: sabbir.amin@goava.com, sabbiramin.cse11ruet@gmail.com 

"""
import json

import redis
from ariadne import load_schema_from_path, QueryType, make_executable_schema, graphql_sync
from ariadne.explorer.playground import ExplorerPlayground

from flask import Flask, request, jsonify

type_defs = load_schema_from_path("../schema.graphql")
query = QueryType()
# mutation = MutationType()

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
app = Flask(__name__)

PLAYGROUND_HTML = ExplorerPlayground(title="Cool API").html(None)


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code


if __name__ == "__main__":
    app.run(
        host='localhost',
        port=5055,
        debug=True)
