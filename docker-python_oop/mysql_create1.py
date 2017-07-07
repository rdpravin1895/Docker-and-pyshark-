#!/usr/bin/python

import docker
import time
import json
from mysql_create import *
client = docker.APIClient(base_url='unix://var/run/docker.sock')

class WpMysql_start(WpMysql):
	
	def __init__(self):
		print "Constructor created for creating Mysql and Wordpress"
	
		
d=WpMysql_start()
list=client.containers(all=True)
mq='mysql' in json.dumps(list)
print mq

if(mq==False):
	d.Mysql_method_create()
	d.Mysql_method_start()
else:
	print "Mysql already exists"
	


list=client.containers(all=True)
wp='wordpress_1' in json.dumps(list)
print wp

if(wp==False):
	d.Wp_method_create()
	d.Wp_method_start()
else:
	print "Wordpress already exists"

