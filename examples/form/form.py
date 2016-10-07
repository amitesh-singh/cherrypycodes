import cherrypy

class Form(object):
    # this is called when you do http://localhost:8080/ or http://192.168.0.109:8080/
    @cherrypy.expose
    def index(self):
        return """
            <html>
            <head></head>
            <body>
            <form method="get" action="mynameis">
              <input type="text" value="Ami" name="name" />
              <button type="submit">Submit!</button>
            </body>
            </html>
        """
    @cherrypy.expose
    def mynameis(self, name="ami"):
        return """
        <html>
        <body>
        <b>My name is %s</b> <br>
        <strike>Learn cherrypy framework </strike>
       </body>
        </html>
        """ % name


if __name__ == "__main__":
    # This will run cherrypy on public interface. by default its bind to localhost:8080
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.quickstart(Form())
