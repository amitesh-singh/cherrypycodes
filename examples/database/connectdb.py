import cherrypy
import MySQLdb

db = None

def connect():
    global db
    # Create a connection and store it in the current thread
    db = MySQLdb.connect('localhost', 'root', '', 'test')

class DbConnect(object):

    @cherrypy.expose
    def index(self):
        c = db.cursor()
        c.execute('select count(*) from pet')
        res = c.fetchall()
        c.close()
        print res
        return """<html>
        <style>
        .button {
            display: inline-block;
            border-radius: 4px;
            background-color: #f4511e;
            border: none;
            color: #FFFFFF;
            text-align: center;
            font-size: 28px;
            padding: 20px;
            width: 200px;
            transition: all 0.5s;
            cursor: pointer;
            margin: 5px;
        }

        .button span {
            cursor: pointer;
            display: inline-block;
            position: relative;
            transition: 0.5s;
        }

.button span:after {
content: ">";
position: absolute;
opacity: 0;
top: 0;
right: -20px;
transition: 0.5s;
}

.button:hover span {
padding-right: 25px;
}

.button:hover span:after {
opacity: 1;
right: 0;
}
        </style>
        <body>
        Hello, you have %d records in your table named 'pet'
        <form method="GET" action="getallrecords">
        <button type="submit" class="button" style="vertical-align:middle">
        <span>List Pets</span>
        </button>
        </form>

        <form method = "GET" action="getalltable">
        <button type="submit" class="button" style="vertical-align:middle">
        <span>List Table</span>
        </button>

        </form>

        </body>
        </html>

        """ % res[0]

    @cherrypy.expose
    def getalltable(self):
        c = db.cursor()
        c.execute('select * from pet')
        res = c.fetchall()
        c.close()

        return """
        <html>
        <body>
        <h1>Table:</h1>
        <h3> %s </h3>
         </body>
        </html>""" % str(res)


    @cherrypy.expose
    def getallrecords(self):
        c = db.cursor()
        c.execute('select * from pet')
        res = c.fetchall()
        c.close()
        #print res
        #print res[0]
        #print res[0][0]
        petsname = ""
        for item in res:
            petsname += str(item[0]) + "<br>"
        return  """
        <html>
        <body>
        Pets are <br>
        <h3> %s </h3>
         </body>
        </html>

        """ % petsname


if __name__ == "__main__":
    # This will run cherrypy on public interface. by default its bind to localhost:8080
    connect()
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.quickstart(DbConnect())
