# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 30 Aug 2023
email: sabbir.amin@goava.com, sabbiramin.cse11ruet@gmail.com

"""

import typing
import redis
import strawberry

REDIS_host = 'localhost'
REDIS_port = 6379
REDIS_db = 0
REDIS_decode_response = True

rr = redis.StrictRedis(host=REDIS_host,
                       port=REDIS_port,
                       db=REDIS_db,
                       decode_responses=REDIS_decode_response)


@strawberry.type
class CommonString:
    response: str


class CommonDict:
    response: dict


@strawberry.type
class Query:
    @strawberry.field
    def set(self,
            name: str,
            value: str,
            ex: typing.Optional[int] = None,
            px: typing.Optional[int] = None,
            nx: typing.Optional[bool] = False,
            xx: typing.Optional[bool] = False,
            keepttl: typing.Optional[bool] = False,
            get: typing.Optional[bool] = False,
            exat: typing.Optional[int] = None,
            pxat: typing.Optional[int] = None
            ) -> CommonString:
        print(name, value, get)
        resp = rr.set(
            name=name,
            value=value,
            ex=ex,
            px=px,
            nx=nx,
            xx=xx,
            keepttl=keepttl,
            get=get,
            exat=exat,
            pxat=pxat
        )
        print('resp:', resp)
        return CommonString(response=resp)

    @strawberry.field
    def get(self, name: str) -> CommonString:
        resp = rr.get(name=name)
        return CommonString(response=resp)

    @strawberry.field
    def info(self) -> CommonString:
        info_dict = rr.info()
        print(info_dict)
        return CommonString(response=str(info_dict))


schema = strawberry.Schema(Query)

from flask import Flask
from strawberry.flask.views import GraphQLView


class Server:
    def __init__(self,
                 host: str = 'localhost',
                 port: int = 5055,
                 debug=True
                 ):
        self.app = Flask(__name__)
        self.host = host
        self.port = port
        self.debug = debug
        self.app.add_url_rule(
            "/graphql",
            view_func=GraphQLView.as_view("graphql_view", schema=schema),
        )

    def run(self):
        self.app.run(
            host=self.host,
            port=self.port,
            debug=self.debug
        )
