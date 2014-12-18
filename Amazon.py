import boto
from boto.ec2 import EC2Connection
import boto.ec2
import time


connect = EC2Connection()

class Amazon:
	def request_instances(num):
		image = "ami-769efd1e"
		subnet = "subnet-e30cccc8"
		security_group_id = "sg-f96f9d9d"
		key = "LabsKey"
		number = num
		reservation = connect.run_instances(image, max_count = number, instance_type = 't2.micro', key_name = key,placement = "us-east-1c" )# Using boto EC2Connection class
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
	def get_instance_details(self):
		reservations = connect.get_all_instances()
		instances = [i for r in reservations for i in r.instances]
		for i in instances:
			print(i.__dict__)
			break
a = Amazon()
a.get_instance_details()
