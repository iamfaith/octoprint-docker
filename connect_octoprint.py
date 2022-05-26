#!/home/faith/miniconda3/bin/python

# /dev/ttyACM0 
OCTOPRINT_URL = 'http://192.168.31.24:9500/api/connection'
API_KEY = 'D907C9FFF9334D92865752432B73C921'
BAUDRATE = 115200


import requests
import sys

port = '/dev/ttyACM0'  #sys.argv[1]
headers = {'X-Api-Key': API_KEY}
json = {
  "command": "connect",
  "port": port,
  "baudrate": BAUDRATE,
}

r = requests.post(
        OCTOPRINT_URL,
        json=json,
        headers=headers
)

if (r.status_code == 204):
    sys.exit(0)
else:
    print(r)
    sys.exit(1)
