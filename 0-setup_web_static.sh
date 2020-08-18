#!/usr/bin/env bash
# this configure a dployd to server.
# check if nginx is already install
if ! command -v Nginx &> /dev/null
then
    # install nginx
    sudo apt-get -y update
    sudo apt-get -y install nginx
    sudo service nginx start
fi
# check if a /data/ exist and create it if not exist.
if [ ! -d /data/ ]
then
    mkdir /data/
fi
# check if a /data/web_static exist and create it if not exist.
if [ ! -d /data/web_static/ ]
then
    sudo mkdir -p /data/web_static/
fi

# check if a /data/web_static/releases/ exist and create it if not exist.
if [ ! -d /data/web_static/releases/ ]
then
    sudo mkdir -p /data/web_static/releases/
fi

# check if a /data/ exist and create it if not exist.
if [ !  -d /data/web_static/releases/ ]
then
    sudo mkdir -p /data/web_static/releases/
fi
    
# check if a /data/web_static/shared/ exist and create it if not exist.
if [ ! -d /data/web_static/shared/ ]
then
    sudo mkdir -p /data/web_static/shared/
fi

# check if a /data/ exist and create it if not exist.
if [ ! -d /data/web_static/releases/test/ ]
then
    sudo mkdir -p /data/web_static/releases/test/
fi

# Create a fake HTML file /data/web_static/releases/test/index.html to test nginx.
sudo echo "<html>" | sudo tee /data/web_static/releases/test/index.html
sudo echo "    <head>" | sudo tee /data/web_static/releases/test/index.html
sudo echo "    </html>" | sudo tee /data/web_static/releases/test/index.html
sudo echo "    <body>" | sudo tee /data/web_static/releases/test/index.html
sudo echo "        Holberton School" | sudo tee /data/web_static/releases/test/index.html
sudo echo "    </body>" | sudo tee /data/web_static/releases/test/index.html
sudo echo "</html>" /data/web_static/releases/test/index.html


# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder.
if [ -L /data/web_static/current ]
then
    sudo rm -f /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
var1="\\\tlocation /hbnb_static {\\n\t\talias /data/web_static/current/;\n\t}"
# sudo sed -i "/server_name _./a\ $var1" /etc/nginx/sites-enabled/default
sudo sed -i "26i $var1" /etc/nginx/sites-enabled/default

# updating changes innginx
sudo service nginx restart
