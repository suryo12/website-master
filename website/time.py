import datetime as dt
from datetime import datetime
from datetime import timedelta, date

start_datedt = dt.datetime(2012, 12,1)
end_datedt = dt.datetime(2012, 12,2)
menit = [10, 20, 30, 40, 50, 59]
jam = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

total_days = (end_datedt - start_datedt).days + 1

for day_number in range(total_days):
    current_date = (start_datedt + dt.timedelta(days=day_number)).date()
    for i in jam:
        for x in menit:
            print current_date
            date = dt.time(i, x)
            print date


z = 'print jam'
print z



