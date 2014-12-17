#!/bin/bash -ex
exec > >(tee /var/log/user-data.log|logger -t user-data -s 2>/dev/console) 2>&1
#wget https://github.com/vlead/setup-ovpl-centos/archive/v1.0.0.tar.gz
echo BEGIN
date '+%Y-%m-%d %H:%M:%S'
yum install -y git
git clone https://github.com/vlead/setup-ovpl-centos.git
git checkout develop

cd setup-ovpl-centos/scripts

./centos_prepare_ovpl.sh
echo END

