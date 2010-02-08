import bottle
bottle.debug(True)

from bottle import route 
from google.appengine.ext.webapp import util 

@route('/')
def hello():
    return "bottle on app engine!"

if __name__ == '__main__':
	util.run_wsgi_app(bottle.default_app())




