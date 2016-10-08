# This is pretty handy in case of knowing the public Ip

import cherrypy
from urllib2 import urlopen

class KnowMyPubIp(object):

   @cherrypy.expose
   def index(self):
      my_ip = urlopen('http://ip.42.pl/raw').read()
      return "public ip is "  + my_ip

cherrypy.config.update({'server.socket_host': '0.0.0.0'})
cherrypy.quickstart(KnowMyPubIp());

