#!/bin/bash

echo ""
echo "Fetching OVPL from GitHub.."
cd /root
git clone https://github.com/vlead/ovpl.git

cd ovpl
echo "changed to OVPL directory.."
echo "Checking out version v1.0.0 .."
git checkout tags/v1.0.0
echo ""

echo "Installing OVPL.."
python setup.py install

echo ""
echo "Congrats! You have setup OVPL successfully!!! :-)"
echo "Now run 'make' from inside the src directory"
echo " of OVPL to start the services."

exit 0
