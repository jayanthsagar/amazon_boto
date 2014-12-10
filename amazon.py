import boto.ec2
#import os
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
	for i in range(0,len(reservations)):
		inst = reservations[i].instances
		
		id = str(inst).split(':')[1].strip(']')
		print id
		#subprocess.check_output("aws ec2 describe-instances --instance-ids "+id)
		#os.system("aws ec2 describe-instances --instance-ids "+id)
		result = subprocess.Popen("aws ec2 describe-instances --instance-ids "+id,stdout=subprocess.PIPE, shell=True)
		(output,status) = result.communicate()
		instance_json = json.dumps(output)
		print type(instance_json)
		inst_json = json.loads(instance_json)
		print inst_json
		f = open('instances/'+id+'.json','w')
		f.write(inst_json)
		f.close()
		
		#print status
		#for j in range(0,len(inst)):
		#	instance = inst[j]
		#	print instance.instance_type
		#	print instance.placement
		#	print instance.state
			


#list_reservations()
#list_instances()
instance_details()
def instance_address():
	address = boto.ec2.address.Address()
	print address

