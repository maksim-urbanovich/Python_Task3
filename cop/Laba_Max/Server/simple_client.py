import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:8000')
#print s.myfunction(2, 3)
x = s.sql_select(2)
print(x)
print(x[0][0], x[0][1])