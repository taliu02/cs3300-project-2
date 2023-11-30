#!/bin/bash
rm service_creds.json
rm .env

wget https://hackgtstoragebucket.s3.amazonaws.com/service_creds.json && wget https://hackgtstoragebucket.s3.amazonaws.com/.env



python3 -m pip install -r requirements.txt

