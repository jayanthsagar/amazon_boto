import boto.ec2
import os
import sys
import subprocess
import json
#import commands
conn = boto.ec2.connect_to_region("us-east-1")
print conn
reservations = conn.get_all_reservations()
reservations
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
	print type(result)

def start_instance():

def stop_instance():

def destroy_instance():


#list_reservations()
#list_instances()
#print instance_details() 
#create_instance()
destroy_instance()
#returns a list of all instance ids and write instance info as json to instances folder
def instance_address():
	address = boto.ec2.address.Address()
	print address

