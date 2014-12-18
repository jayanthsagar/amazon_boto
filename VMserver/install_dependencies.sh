#!/bin/bash

meta_dir="../meta"
yum -y update
echo ""
echo "Setting up EPEL repo.."
#wget http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm
rpm -ivh $meta_dir/epel-release-6-8.noarch.rpm
#rm epel-release-6.8.noarch.rpm

echo ""
echo "Installing dependencies.. yum -y install gcc python-devel.x86_64 python-pip ssh git"
yum -y  install gcc python-devel.x86_64 python-pip ssh git wget
python get-pip.py
python setup.py install
exit 0

