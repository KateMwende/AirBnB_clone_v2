#!/usr/bin/env bash
#script that sets up your web servers for the deployment of web_static

sudo apt -y update
sudo apt -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/current
echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/  /data/web_static/current
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/

sudo echo “
location /hbnb_static {
    alias /data/web_static/current;
    index index.html index.htm;
}” >> /etc/nginx/sites-available/default
sudo service nginx restart
