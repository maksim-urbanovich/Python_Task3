from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from mySql_Python_Select import sql_insert, sql_select

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8000),
                            requestHandler=RequestHandler)


def myfunction(x, y):
    return x+y
server.register_function(sql_insert)
server.register_function(sql_select)

# Run the server's main loop
server.serve_forever()