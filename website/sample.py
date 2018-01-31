import datetime as dt

x = 'Coba print tanggal'
print x

start_datedt = dt.datetime(2012, 12,1)
end_datedt = dt.datetime(2012, 12,5)

total_days = (end_datedt - start_datedt).days + 1 #inclusive 5 days

for day_number in range(total_days):
    current_date = (start_datedt + dt.timedelta(days = day_number)).date()
    print current_date

