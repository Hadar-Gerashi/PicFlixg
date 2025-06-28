#!/bin/bash
# build.sh

# Install Microsoft ODBC Driver
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /etc/apt/trusted.gpg.d/microsoft.asc.gpg
curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/msprod.list
apt-get update
ACCEPT_EULA=Y apt-get install -y msodbcsql18

# Install unixODBC
apt-get install -y unixodbc-dev

# Install Python dependencies
pip install -r requirements.txt
