import requests
import json
import datetime as dt
from datetime import datetime, date, time

server_domain = 'http://localhost:8000/'
app = 'landslide/api/'


def post_data():
    url = server_domain + app
    headers = {'content-type': 'application/json'}
    data = {#"node_name" : "Magelang1",
            #"location" : "Magelang Km 10",
            "node_id" : 1,
            "timestamp" : dt.datetime.now().isoformat(),
            #"timestamp" : datetime.datetime.now().isoformat(),
            "vibration": "56",
            "coordinate_x" : "45",
            "coordinate_y" : "11",
            "coordinate_z" : "78",
            #for x in range(1, 30):
            "tanggal": dt.date(2018, 01, 21).isoformat(),
            "waktu" : dt.time(11, 15).isoformat()
            # "tanggal" : datetime.date.today().isoformat(),
            #"waktu" : datetime.time.now().isoformat()
            #tanggal = models.DateField(db_index=True, null=True, default=None)
            #waktu = models.TimeField(db_index=True, null=True, default=None)
          }

    response = requests.post(url, data=json.dumps(data), headers =headers)

    if response.status_code != 201:
        print('Error: {}'.format(response.text))
    else:
        print('Created: {}'.format(json.loads(response.text)))


if __name__ == '__main__':
    post_data()
