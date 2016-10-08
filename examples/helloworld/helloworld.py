import cherrypy

class helloworld(object):
    # this is called when you do http://localhost:8080/ or http://192.168.0.109:8080/ or http://localhost/index or http://192.168.0.101/index.
    @cherrypy.expose
    def index(self):
       return "Hello World!"
    # /versioninfo
    @cherrypy.expose
    def versioninfo(self):
        return "running cherrypy version 8.1.1"
    # this is called at http://localhost:8080/mynameis?name="ami"
    @cherrypy.expose
    def mynameis(self, name):
        return "my name is " + name

if __name__ == "__main__":
    # This will run cherrypy on public interface. by default its bind to localhost:8080
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.quickstart(helloworld())
