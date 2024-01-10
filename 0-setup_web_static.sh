#!/usr/bin/env bash
# 0-setup_web_static.sh

sudo apt-get update -y
sudo apt-get install nginx -y
mkdir -p -m=755 /data/web_static/{releases/test,shared} || exit 0
sudo echo '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' > /data/web_static/releases/test/index.html
link_path="/data/web_static/current"
target_path="/data/web_static/releases/test/"

sudo ln -fs "$target_path" "$link_path"
sudo chown -hR ubuntu:$ubuntu /data/
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
exit 0
