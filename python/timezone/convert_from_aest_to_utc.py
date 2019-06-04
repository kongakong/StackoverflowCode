#! /usr/bin/env python3
import time
from datetime import datetime
from dateutil import tz

to_zone = tz.gettz('UTC')
from_zone = tz.gettz('AUstralia/Sydney')

from_time = datetime.strptime('2019-06-03 05:00:00', '%Y-%m-%d %H:%M:%S')
from_time = from_time.replace(tzinfo=from_zone)

to_time = from_time.astimezone(to_zone)
print(to_time)
print(time.mktime(to_time.timetuple()))
