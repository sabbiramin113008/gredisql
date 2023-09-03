## GredisQL
A GraphQL interface for Redis Database. 

##  Motivation
1. I was bored, been sick for a while, had to lie on the bed. So I needed to create something. 
2. Redis has Web interface ( actually a REST interface), so I urged to build one in GraphQL. 
3. There are some pretty amazing GraphQL libraries around python echo system, I wanted to try them. 
4. Last but not least, jump into quick coding session, engage and nurture the human mind. LOL

## Design Philosophy
1. All the data `mutation` and `query` are not separated here by action and most probably all the actions are performed via `query` operation.
2. Technically `all` the requests sent to the GraphQL `server` was in `POST`, so I was initially okay with the implementation. 
3. `Strawberry-Graphql` is kind of server agnostic so either you can use `ASGI` or `WSGI` counterpart. 
4. Currently limiting the implementation with `WSGI` server, but I've plan to adopt `ASGI` in the journey, to support `subscription`. 
5. Not `all` Redis commands are found in the implementation, I'll try to cover it in the process. 

## Inspiration and Tools I used

## Features and Future Plans

## Quick Starting the GraphQL Server
```python
if __name__ == "__main__":
    from gredisql.core import Server

    server = Server()
    server.run()
```
You can specify the `host`, `port` and `debug` mode as you like. 