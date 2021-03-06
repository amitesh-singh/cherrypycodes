import cherrypy

class Form(object):
    # this is called when you do http://localhost:8080/ or http://192.168.0.109:8080/
    @cherrypy.expose
    def index(self):
        return """
            <html>
            <head></head>
            <body>
            <form method="get" action="ledOn">
              <button type="submit" name="name">Led On</button>
              </form>
            <form method ="get" action="ledOff">
            <button type="submit" name="name">Led Off</button>
            </form>
            </body>
            </html>
        """
    @cherrypy.expose
    def ledOn(self, name="ok"):
        return "Led is On"

    @cherrypy.expose
    def ledOff(self, name="notok"):
        return "Led is Off" + name


if __name__ == "__main__":
    # This will run cherrypy on public interface. by default its bind to localhost:8080
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.quickstart(Form())
