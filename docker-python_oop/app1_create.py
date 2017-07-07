import docker
client = docker.APIClient(base_url='unix://var/run/docker.sock')

class App1:
	
	def __init__(self):
		print "Constructor for app1"
	
	def App1_method_create(self):
		
		client.create_container("load-balanced-app",name="app_1",detach=True,
						environment={"MESSAGE":"First instance"},
						host_config=client.create_host_config(port_bindings={8080:8081}))
						
	def App1_method_start(self):
		
		client.start("app_1")

class App2:
	
	def __init__(self):
		print "Constructor for app2"
	
	def App2_method_create(self):
		
		client.create_container("load-balanced-app",name="app_2",detach=True,
						environment={"MESSAGE":"Second instance"},
						host_config=client.create_host_config(port_bindings={8080:8082}))
						
	def App2_method_start(self):
		
		client.start("app_2")
		
	def App2_method_stop(self):
		
		client.stop("app_2")
		client.remove_container("app_2")
		
class Nginx_lb:
	
	def __init__(self):
		print "Constructor for Nginx_lb"
		
	def Nginx_method_create(self):
		
		client.create_container("load-balance-nginx",name="nginx_lb",detach=True,
						ports=[80],host_config=client.create_host_config(port_bindings={80:8080}))
		
	def Nginx_method_start(self):
		
		client.start("nginx_lb")
		
	def Nginx_method_stop(self):
		
		client.stop("nginx_lb")
		client.remove_container("nginx_lb")

