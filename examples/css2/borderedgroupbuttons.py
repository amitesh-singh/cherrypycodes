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
            border: 1px solid green;
            color: white;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            cursor: pointer;
            float: left;
        }

    .button:hover {
        background-color: #3e8e41;
    }
        </style>

        </head>

        <body>
        <button class="button">button1</button>
        <button class="button">button2</button>
        <button class="button">button3</button>
        <button class="button">button4</button>
        <button class="button">button5</button>

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
