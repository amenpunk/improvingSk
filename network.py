#!/usr/bin/python3
import requests
import socket
localhost = socket.gethostbyname('localhost')

def check_localhost(host):
    return str(socket.gethostbyname(host)) == '127.0.0.1';

def check_connectivity():
    return requests.get("http://www.google.com").status_code == 200 

