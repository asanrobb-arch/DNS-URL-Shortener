#!/bin/bash

apt-get update
apt-get install -y python3-pip python3-venv

pip install -r /vagrant/requirements.txt

python3 /vagrant/gestor_dns.py

nohup python3 /vagrant/app.py
