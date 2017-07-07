import docker

client = docker.APIClient(base_url='unix://var/run/docker.sock')

client.exec_create("tns_app1_1",cmd="apk update;apk add -y tcpdump net-tools iptables",privileged=True)

client.exec_create("tns_app2_1",cmd="apk update;apk add -y tcpdump net-tools iptables",privileged=True)

client.exec_create("tns_db1_1",cmd="apk update;apk add -y tcpdump net-tools iptables",privileged=True)

client.exec_create("tns_db2_1",cmd="apk update;apk add -y tcpdump net-tools iptables",privileged=True)

client.exec_create("tns_db3_1",cmd="apk update;apk add -y tcpdump net-tools iptables",privileged=True)

client.exec_create("tns_lb1_1",cmd="apk update;apk add -y tcpdump net-tools iptables",privileged=True)

client.exec_create("tns_lb2_1",cmd="apk update;apk add -y tcpdump net-tools iptables",privileged=True)

apt-get update;apt-get install -y tcpdump net-tools iptables