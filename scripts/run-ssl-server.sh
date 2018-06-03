#!/bin/sh

# use self-signed certificate
#python  manage.py runsslserver  0.0.0.0:8000

# use `Let's Encrypt` certificate
python manage.py runsslserver 0.0.0.0:8000 --certificate  /webapps/ssl/fullchain.pem --key /webapps/ssl/privkey.pem
