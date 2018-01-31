import requests
import json
import datetime as dt
from datetime import datetime
from datetime import timedelta, date
import random

server_domain = 'http://localhost:8000/'
app = 'smart/api/'

start_datedt = dt.datetime(2018, 1,21)
end_datedt = dt.datetime(2018, 1,27)
menit = [10, 20, 30, 40, 50, 59]
jam = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

total_days = (end_datedt - start_datedt).days + 1
def post_data():
    url = server_domain + app
    headers = {'content-type': 'application/json'}
    for day_number in range(total_days):
        current_date = (start_datedt + dt.timedelta(days=day_number)).date()
        for i in jam:
            for x in menit:


                data = {#"node_name" : "Magelang1",
                        #"location" : "Magelang Km 10",
                        "node_id": 1,
                        "tegangan": random.randint(220, 240),
                        "arus": random.randint(100, 500),
                        "daya": random.randint(1000, 2000),
                        "tanggal": current_date.strftime("%Y-%m-%d"),
                        "waktu": dt.time(i, x).isoformat()
                }
                response = requests.post(url, data=json.dumps(data), headers=headers)

                if response.status_code != 201:
                    print('Error: {}'.format(response.text))
                else:
                    print('Created: {}'.format(json.loads(response.text)))
                # "tanggal" : datetime.date.today().isoformat(),
                #"waktu" : datetime.time.now().isoformat()

    #response = requests.post(url, data=json.dumps(data), headers =headers)




if __name__ == '__main__':
    post_data()