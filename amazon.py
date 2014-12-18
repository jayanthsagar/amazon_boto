import boto
from boto.ec2 import EC2Connection
import boto.ec2
import os
import sys
import subprocess
import json
import time
#import commands
conn = boto.ec2.connect_to_region("us-east-1")
print conn
reservations = conn.get_all_reservations()
print reservations
def list_reservations():
	for i in range(0,len(reservations)):
		print reservations[i]
def list_instances():
	for i in range(0,len(reservations)):
		print reservations[i].instances
def instance_details():
	instances_id = []
	for i in range(0,len(reservations)):
		inst = reservations[i].instances
		
		id = str(inst).split(':')[1].strip(']')
		instances_id.append(id)
		#print id # I am refering every instance using its id
		#subprocess.check_output("aws ec2 describe-instances --instance-ids "+id)
		#os.system("aws ec2 describe-instances --instance-ids "+id)
		result = subprocess.Popen("aws ec2 describe-instances --instance-ids "+id,stdout=subprocess.PIPE, shell=True)
		(output,status) = result.communicate()
		instance_dumps_json = json.dumps(output) #encoding
		#print type(instance_json)
		instance_loads_json = json.loads(instance_dumps_json) #decoding
		#print type(inst_json)
		f = open('instances/'+id+'.json','w')
		f.write(instance_loads_json)
		f.close()
		
		#print status
		#for j in range(0,len(inst)):
		#	instance = inst[j]
		#	print instance.instance_type
		#	print instance.placement
		#	print instance.state
	return instances_id	
def create_instance():
	#image = conn.get_all_images() #for getting ami stored in amazon account
	image = "ami-bc8131d4" #for now using same ami to create instance, later will get our own ami with necessary modifications
	subnet = "subnet-7902f252"
	security_group_id = "sg-c614f5a2"
	key = "cli-test" #using cli-test.pem for now
	result = os.system("aws ec2 run-instances --image-id "+image+" --count 1 --instance-type t1.micro  --subnet-id "+subnet+" --security-group-ids "+security_group_id+" --associate-public-ip-address --key-name "+key)
	# Using awscli command
	print type(result)

def create_instance_with_userdata(num):
	image = "ami-769efd1e"
	subnet = "subnet-e30cccc8"
	security_group_id = "sg-f96f9d9d"
	key = "LabsKey"
	number = num
	#test_script = """#!/bin/bash -ex
	#exec > >(tee /var/log/user-data.log|logger -t user-data -s 2>/dev/console) 2>&1
	#wget https://github.com/vlead/setup-ovpl-centos/archive/v1.0.0.tar.gz
	#echo BEGIN
	#date '+%Y-%m-%d %H:%M:%S'
	#yum install -y git
	#git clone https://github.com/vlead/setup-ovpl-centos.git
	#git checkout develop

	#cd setup-ovpl-centos/scripts

	#./centos_prepare_ovpl.sh
	#echo END"""

	ec2conn = EC2Connection()
	reservation = ec2conn.run_instances(image, max_count = number, instance_type = 't2.micro', key_name = key,placement = "us-east-1c" )
	# Using boto EC2Connection class
	for instance in reservation.instances:
		if instance.update() == u'running':
			print "Instance "+instance+" is running"  
			break
		else:
			while 1:
				time.sleep(5)
				if instance.update() == u'running':
					print "Instance ",instance," is running"
					break
				else:
					continue
	#while not instance.update() == 'running':
	#	time.sleep(5)
	
def start_instance():
	pass
def stop_instance():
	pass
def destroy_instance():
	pass


#list_reservations()
#list_instances()
print instance_details() 
#create_instance()
#destroy_instance()
#create_instance_with_userdata(1)
#returns a list of all instance ids and write instance info as json to instances folder
def instance_address():
	address = boto.ec2.address.Address()
	print address

