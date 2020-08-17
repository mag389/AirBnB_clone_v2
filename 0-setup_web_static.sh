#!/usr/bin/env bash
# prepare our web servers
# install nginx if not installed
sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'
sudo service nginx restart
# create folder /data/ if not exists
sudo mkdir -p /data/
# create folder /data/web_static/ if not exists
sudo mkdir -p /data/web_static/
# create folder /data/web_static/releases/ if not exists
sudo mkdir -p /data/web_static/releases/
# create folder /data/web_static/shared/ if not exists
sudo mkdir -p /data/web_static/shared
# create folder /data/web_static/releases/test/ if not exists
sudo mkdir -p /data/web_static/releases/test/
# create fake html file /data/web_static/releases/test/index.hmtl
# 	to test nginx config
sudo touch /data/web_static/releases/test/index.html
sudo echo "test passed" | sudo tee /data/web_static/releases/test/index.html
# create symbolic link /data/web_static/current to /data/web_static/releases/test/
# 	recreate if it exists
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# change ownership of /data/ to ubuntu and group
sudo chown -R ubuntu:ubuntu /data/
# update nginx to serve /data/web_static/current/ to hbnb_static
# shellcheck disable=SC2016
newstring='server {
	listen 80 default_server;
	listen [::]:80 default_server;
	location /hbnb_static {
	alias /data/web_static/current/;
	index index.html;
	}
	location /tester {
        alias /var/www/html/;
        index tester.html;
        }
        rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
        add_header  X-Served-By $hostname;
	error_page 404 /not_found.html;
	location = /not_found.html {
		root /usr/share/nginx/html;
		internal;
	}
	root /var/www/html;
	index index.html index.htm index.nginx-debian.html;
	server_name _;
	location / {
		try_files $uri $uri/ =404;
	}
}'
sudo echo "$newstring" | sudo tee /etc/nginx/sites-available/default
sudo service nginx restart
