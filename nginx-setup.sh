#!/bin/bash

echo "Installing nginx..."
sudo apt-get update
sudo apt-get install nginx -y 

echo "Copying website..."
sudo cp /home/ubuntu/web/* /var/www/html/

echo "Restarting nginx..."
sudo service nginx restart 

echo "Done"
