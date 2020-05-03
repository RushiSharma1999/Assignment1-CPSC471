# -*- coding: utf-8 -*-

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("user", "Passwd", "/home/directory", perm="elradfmw") #user, pass, directory
authorizer.add_anonymous("/home", perm="elradfmw") #enter directory

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("127.0.0.1", 1026), handler) #IP Address
server.serve_forever()
