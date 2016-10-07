# put style.css in public/css/ folder

import cherrypy
import os, os.path

class Form(object):
    # this is called when you do http://localhost:8080/ or http://192.168.0.109:8080/
    @cherrypy.expose
    def index(self):
        return """
            <html>
            <head>
            <style>
            .button {
                background-color: #4CAF50; /*Green*/
                border: none;
                color: white;
                padding: 15px 32px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
            }

            .button1 {background-color: #4CAF50;} /* Green */

            .button2 {background-color: #008CBA;} /* Blue */

            .button3 {background-color: #f44336;} /* Red */

            .button4 {
                background-color: #e7e7e7;
                color: black;
                border: none;
                padding: 15px 32px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;

                } /* Gray */

            .button5 {background-color: #555555;
                font-size: 24px} /* Black */

            /* rounded size buttons */
            .button6 {
                border-radius: 12px;
                background-color: #e7e7e7;
                color: black;
                border: none;
                padding: 15px 32px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 15px;
                cursor: pointer;
            }
            .button7 {
                border-radius: 50%;
                background-color: #e7e7e7;
                color: black;
                border: none;
                padding: 15px 32px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 15px;
                cursor: pointer;
            }
            /* Colored button borders */
            .button8 {
                background-color: white;
                color: black;
                border: 2px solid #4CAF50; /* Green */
            }
            /* Hoverable buttons */
            .button {
    background-color: #4CAF50; /* Green */
    border: none;
    color: white;
    padding: 16px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    -webkit-transition-duration: 0.4s; /* Safari */
    transition-duration: 0.4s;
    cursor: pointer;
}
.button9 {
    background-color: white;
    color: black;
    border: 2px solid #4CAF50;
}

.button9:hover {
    background-color: #4CAF50;
    color: white;
}




            </style>
            </head>
            <body>
            <form method="get" action="mynameis">
              <input type="text" value="Ami" name="name" />
              <button type="submit" class="button">Submit!</button>
              <button type="submit" class="button1">Submit!</button>
              <button type="submit" class="button2">Submit!</button>
              <button type="submit" class="button3">Submit!</button>
              <button type="submit" class="button4">Submit!</button>
              <button type="submit" class="button5">Submit!</button>
              <button type="submit" class="button6">Round</button>
               <button type="submit" class="button7">50 % Round</button>
               <button type="submit" class="button8">Colored border</button>
               <button type="submit" class="button9">Hover Button</button>
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
