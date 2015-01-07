import boto
from boto.ec2 import EC2Connection
import boto.ec2
import boto.ec2.networkinterface
import time
from pprint import pprint
#import os
#import sys


connect = EC2Connection()

class Amazon:
	def request_instances(self, num):
		image = "ami-769efd1e"
		subnet = "subnet-e30cccc8"
		security_group_id = ['sg-f96f9d9d']
		key = "LabsKey"
		number = num
		interface = boto.ec2.networkinterface.NetworkInterfaceSpecification(subnet_id=subnet, groups=security_group_id, associate_public_ip_address=True)
		interfaces = boto.ec2.networkinterface.NetworkInterfaceCollection(interface)
		reservation = connect.run_instances(image, max_count = number, instance_type = 't2.micro', key_name = key,placement = "us-east-1c", network_interfaces = interfaces )# Using boto EC2Connection class
		#reservation = os.system("aws ec2 run-instances --image-id "+image+" --count "+str(num)+" --instance-type t1.micro  --subnet-id "+subnet+" --security-group-ids "+security_group_id+" --associate-public-ip-address --key-name "+key)

		for instance in reservation.instances:
			if instance.update() == u'running':
				print "Instance "+str(instance)+" is running"  
				break
			else:
				while 1:
					time.sleep(5)
					if instance.update() == u'running':
						print "Instance "+str(instance)+" is running"
						break
					else:
						continue
	def get_instance_details(self):
		reservations = connect.get_all_instances()

		instances = [i for r in reservations for i in r.instances]
		print instances
		print "######################################################################"
		for i in instances:
			#pprint(i.__dict__)
			details = i.__dict__
			keys = details.keys()
			#print details.get('vpc_id')
			if "ip_address" in keys and str(details.get('_state'))=='running(16)' and details.get('vpc_id')=='vpc-9aa038ff':
				print details.get('ip_address')

			

	def get_instances_on_vpc(self,vid):
		vpc_id = vid
		reservations = connect.get_all_instances()

		instances = [i for r in reservations for i in r.instances]
		print instances
		print "######################################################################"
		#a  = []
		f = open("result.html",'w')
		f.write("""<table style="width:100%">
  						<tr>
    						<td>Public-ip</td>
    						<td>Private-ip</td>		
    						<td>instance-id</td>
    					</tr>""")
		for i in instances:
			#pprint(i.__dict__)
			details = i.__dict__
			keys = details.keys()
			if "ip_address" in keys and str(details.get('_state'))=='running(16)' and details.get('vpc_id')=='vpc-9aa038ff':
				f.write("""<tr>
					           <td>%s</td>
    						   <td>%s</td>		
    						   <td>%s</td>
    					    </tr>""",str(details.get('ip_address')).strip("u"),str(details.get('private_ip_address')).strip("u"),str(details.get('id')).strip("u"))
		f.write("""
			</table>""")
		f.close()
		return True #details.get('ip_address')


a = Amazon()
#.request_instances(2)
#a.get_instance_details()
#a.get_instances_on_vpc('vpc-9aa038ff')