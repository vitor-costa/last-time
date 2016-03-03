from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from app import app
import os

http_server = HTTPServer(WSGIContainer(app))
port = int(os.environ.get("PORT", 5000))
http_server.listen(port)
IOLoop.instance().start()