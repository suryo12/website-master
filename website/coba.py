import time, datetime
from datetime import timedelta, date
#use time.time() on Linux

start = time.clock()

for x in range(1000):
    pass
stop = time.clock()

print stop-start

start = time.clock()
for x in xrange(1000):
    pass
stop = time.clock()

print stop-start

x = 'Coba print tanggal'
print x

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)

start_date = date(2012, 12,1)
end_date = date(2012, 12,5)
for single_date in daterange(start_date, end_date):
    print single_date.strftime("%Y-%m-%d")

x = 'Coba print tanggal yang lain'
print x

date = datetime.date(2003,8,1)
for i in range(5):
    date += datetime.timedelta(days=1)
    print(date)

