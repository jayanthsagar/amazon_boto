#!/bin/python
# Services exposed by the VM Manager
# The REST url :
# http://host-name/api/1.0/disk-usage
# http://host-name/api/1.0/running-time
# http://host-name/api/1.0/mem-usage
# http://host-name/api/1.0/running-processes
# http://host-name/api/1.0/cpu-load
# http://host-name/api/1.0/execute/<command>
import urlparse
import os
import os.path
import json
# bunch of tornado imports
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
import Amazon
import logging
define("port", default=8000, help="run on the given port", type=int)
class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('index.html')
	def post(self):
		post_data = dict(urlparse.parse_qsl(self.request.body))
		c = Amazon.Amazon()
		#self.write(c.create_instances(post_data['number_of_vm']))
		c.create_instances(post_data['number_of_vm'])
		result = c.get_instances_on_vpc('vpc-9aa038ff')
		if(result == True)
		    self.render('result.html')
		print "Got request for "+post_data['number_of_vm']+"VMs"

class VMDetails(tornado.web.RequestHandler):
    def get(self, command):
    	result = c.get_instances_on_vpc('vpc-9aa038ff')
		if(result == True)
		    self.render('result.html')
		        

if __name__ == "__main__":
	tornado.options.parse_command_line()
	app = tornado.web.Application(
		handlers=[
			(r"/", MainHandler),
			(r"/VMDetails", VMDetails)
		],
		template_path=os.path.join(os.path.dirname(__file__), "templates"),debug = True)
	http_server = tornado.httpserver.HTTPServer(app)
	current_file_path = os.path.dirname(os.path.abspath(__file__))
	options.port = 8080
	logging.info("VMserver: It will run on port : "+str(options.port))
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()