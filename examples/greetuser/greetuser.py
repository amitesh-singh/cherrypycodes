import cherrypy


class GreetUser(object):
    @cherrypy.expose
    def index(self):
        return """ <html>
            <head> </head>
            <body>
            <form method="GET" action="greetuser">
                <input type="text" name="username" />
                <button type="submit">Submit</button>
            </form>
            </body>
        </html>
        """
    @cherrypy.expose
    def greetuser(self, username=None):
        if username:
            return "Welcome %s here, whats up!" % username
        else:
            return "Please go back and enter your name"

if __name__ == "__main__":
    # This will run cherrypy on public interface. by default its bind to localhost:8080
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.quickstart(GreetUser())
