#python program to create objects and start app1,app2 and loadbalanceer nginx_lb based on threshold
import docker
import time
import pyshark
import json
import ast	
import threshold
from app1_create import *
client = docker.APIClient(base_url='unix://var/run/docker.sock')

class App1_start(App1,App2):
	
	def __init__(self):
		print "contructor created for App"
		
e=App1_start()

list=client.containers(all=True)
ap1='app_1' in json.dumps(list)
print ap1

if(ap1==False):
	e.App1_method_create()
	e.App1_method_start()
else:
	print "App_1 already exists"
	
class Nginx_start(Nginx_lb):

	def __init__(self):
		print "contructor created for nginx_lb"

ngn=Nginx_start()

capture = pyshark.LiveCapture(interface='docker0')
capture.sniff(timeout=5)
count=0
th=threshold.threshold_rate
length=0

for pkt in capture:
	
	if("IP" in str(pkt.layers) and "IPV6" not in str(pkt.layers)):
		
		if(pkt.ip.src == '172.17.0.2' and int(pkt.length) > th):

			count=count+1
			length+=float(pkt.length)
			print count


			if(count==10):
				
				if((length/count)>=th):
					
					print (length/count)
					print"Loadbalancing required"
					list=client.containers(all=True)
					ap='app_2' in json.dumps(list)
					print ap

					ng='nginx_lb' in json.dumps(list)
					print ng

					if(ap==False):

						e.App2_method_create()
						e.App2_method_start()
					
					if(ng==False):
						ngn.Nginx_method_create()
						ngn.Nginx_method_start()
						print "Loadbalancer has been created"
					
				else:
					
					print (length/count)
					print"Loadbalancing not required"
					list=client.containers(all=True)
					ap='app_2' in json.dumps(list)
					print ap

					ng='nginx_lb' in json.dumps(list)
					print ng

					if(ap==True):
						e.App2_method_stop()
						
					if(ng==True):
						ngn.Nginx_method_stop()
					
				count=0
				length=0
					
