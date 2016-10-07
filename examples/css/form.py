# put style.css in public/css/ folder

import cherrypy
import os, os.path

class Form(object):
    # this is called when you do http://localhost:8080/ or http://192.168.0.109:8080/
    @cherrypy.expose
    def index(self):
        return """
            <html>
            <head><link href="/static/css/style.css" rel="stylesheet"></head>
            <body>
            <h1> i am green </h1>
            <p>This paragraph text color is red and its center aligned.</p>
            <form method="get" action="mynameis">
              <input type="text" value="Ami" name="name" />
              <button type="submit" class="button">Submit!</button>
            </body>
            </html>
        """
    @cherrypy.expose
    def mynameis(self, name):
        return "my name is %s" % name


if __name__ == "__main__":
    # This will run cherrypy on public interface. by default its bind to localhost:8080
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    # Now 127.0.0.1:9090/ will work.
    cherrypy.config.update({'server.socket_port' : 9090})
    # cherrypy.quickstart(Form())
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    cherrypy.quickstart(Form(), '/', conf)
