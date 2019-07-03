# Tutorial video dari https://youtu.be/eirjjyP2qcQ

import datetime
import pytz

today = datetime.date.today()

# print(today)
# print(today.month)
# print(today.day)
# print(today.weekday())
# print(today.isoweekday())

tdelta = datetime.timedelta(days=7)

print(today + tdelta)

# date2= date1 + timedelta
# timedelta = date1 + date2

bday = datetime.date(2019,10,25)
till_bday = bday - today
print(till_bday.days)

# Time

t = datetime.time(9, 30, 45, 100000)
dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)

datetz = datetime.datetime(2019, 7, 1, 17, 51, 25, tzinfo=pytz.UTC)
dt_nowutc = datetime.datetime.now(tz=pytz.UTC)
dt_now_jakarta = dt_nowutc.astimezone(pytz.timezone('Asia/Jakarta')) 
print(datetz)
print(dt_nowutc)
print(dt_now_jakarta)

print(dt_nowutc.strftime('%H:%M'))