
import docker
import time
import json
client = docker.APIClient(base_url='unix://var/run/docker.sock')

class WpMysql:
	
	def __init__(self):
		print "Constructor created for creating Mysql and Wordpress"
		
	
	def Mysql_method_create(self):
		
		client.create_container("mysql",name="mysql",detach=False,
						environment={"MYSQL_ROOT_PASSWORD":"12345"},
						networking_config=client.create_networking_config({
							'net_1':client.create_endpoint_config()}))
						
	def Mysql_method_start(self):
		client.start("mysql")
		time.sleep(10)
	
	
	def Wp_method_create(self):
		global wordpress_host_config
		wordpress_host_config=client.create_host_config(port_bindings={80: ('127.0.0.1', 5020)})

		client.create_container("wordpress",name="wordpress_1",detach=True,
						environment={"WORDPRESS_DB_USER":"root","WORDPRESS_DB_PASSWORD":"12345"},
						networking_config=client.create_networking_config({
							'net_1':client.create_endpoint_config(links=[('mysql','link_1')])}),
								host_config=client.create_host_config(port_bindings={80: ('127.0.0.1', 5020)}))
	
	def Wp_method_start(self):
		client.start("wordpress_1")
		time.sleep(5)