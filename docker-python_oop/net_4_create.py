#python class for net_4 bridge network
import docker
client = docker.APIClient(base_url='unix://var/run/docker.sock')

class net_4:
	
	def __init__(self):
		print "Constructor created for creating net_4"
		
	def Net_4_method(self):
		client.create_network("net_4",driver="bridge")
		
