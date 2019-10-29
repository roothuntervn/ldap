#! /bin/bash

docker build -t ldapchal .
docker run -p 127.0.0.1:3890:389 -p 127.0.0.1:1111:80 --name ldap -ti -d -v $(pwd)/htdocs:/var/www/html ldapchal
