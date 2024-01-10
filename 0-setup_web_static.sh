#!/usr/bin/env bash
# 0-setup_web_static.sh

sudo apt-get update -y
sudo apt-get install nginx -y
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir /data/web_static/shared/
sudo echo "I'm from nginx server" > /data/web_static/releases/test/index.html
link_path="/data/web_static/current"
target_path="/data/web_static/releases/test/"

# Remove the symbolic link if it already exists
if [ -L "$link_path" ]; then
    sudo rm "$link_path"
fi

# Create a new symbolic link
sudo ln -s "$target_path" "$link_path"
sudo chown -R $USER:$USER /data/
sudo echo 'server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    server_name _;
    add_header X-Served-By $HOSTNAME;

    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html index.htm index.nginx-debian.html;
        try_files $uri $uri/ =404;
    }

    location / {
        try_files $uri $uri/ =404;
    }
}' > /etc/nginx/sites-available/default
sudo service nginx restart

