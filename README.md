## GredisQL
A GraphQL interface for Redis Database. 

## Quick Starting the GraphQL Server
```python
if __name__ == "__main__":
    from gredisql.core import Server

    server = Server()
    server.run()
```
You can specify the `host`, `port` and `debug` mode as you like. 