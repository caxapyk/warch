from livereload import Server
from wsgi import application


server = Server(application)
server.serve(host='localhost', port=5000)