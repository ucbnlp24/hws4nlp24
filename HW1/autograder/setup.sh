#!/bin/bash

# Update package lists
apt-get update

# Install Python 3 and pip
apt-get install -y python3
apt-get install -y python3-pip

# Navigate to the autograder source directory
cd /autograder/source

# Install Python dependencies from a requirements.txt file
pip3 install -r requirements.txt