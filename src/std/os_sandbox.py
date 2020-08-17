import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

print(os.name)

filename = 'testfile.txt'
t = time.ctime(path.getmtime(filename))
print(t)
print(datetime.datetime.fromtimestamp(path.getmtime(filename)))

td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime(filename))
print(td)
print(str(td.total_seconds()))