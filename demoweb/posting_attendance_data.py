import requests
import json
import time, datetime

server_domain = 'http://localhost:8000/'
app = 'absensi/api/'

def post_data():
	url = server_domain+app
	headers = {'content-type': 'application/json'}
	data={"timestamp" 			: datetime.datetime.now().isoformat(),
  			"name": "newuser",
    		"student_id"	: "87654321",
    		"university_id"	: "88888888"
		}
	response = requests.post(url, data=json.dumps(data), headers = headers)

	if response.status_code != 201:
		print('Error: {}'.format(response.text))
	else:
		print('Created: {}'.format(json.loads(response.text)))




if __name__ == '__main__':
	post_data()
	
