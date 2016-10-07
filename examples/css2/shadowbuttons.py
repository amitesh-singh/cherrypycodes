# put style.css in public/css/ folder

import cherrypy
import os, os.path

class Form(object):

    @cherrypy.expose
    def index(self):
        return """
        <html>
        <head>

        <style>
        .button {
    background-color: #4CAF50; /* Green */
    border: none;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    -webkit-transition-duration: 0.4s; /* Safari */
    transition-duration: 0.4s;
}

.button1 {
    box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
}

.button2:hover {
    box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24),0 17px 50px 0 rgba(0,0,0,0.19);
}
        </style>

        </head>

        <body>
        <button class="button button1">Shadow Button</button>
<button class="button button2">Shadow on Hover</button>

        </body>
        </html>
        """


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
