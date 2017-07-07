import docker
import time
from app1_create import *
client = docker.APIClient(base_url='unix://var/run/docker.sock')

class App1_start(App1,App2):
	
	def __init__(self):
		print "contructor created for App"
		
e=App1_start()

e.App1_method_create()
e.App1_method_start()

e.App2_method_create()
e.App2_method_start()

class Nginx_start(Nginx_lb):
	
	def __init__(self):
		print "contructor created for nginx_lb"
		
ngn=Nginx_start()
ngn.Nginx_method_create()
ngn.Nginx_method_start()