from livereload import Server
from wsgi import application


if __name__ == '__main__':
    application.debug = True
    server = Server(application)
    server.serve(host='localhost', port=5000)