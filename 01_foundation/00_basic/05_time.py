import time
import arrow
from datetime import datetime, timedelta

localtime = time.localtime(time.time())
print("Local current time :", localtime)

localtime = time.asctime(time.localtime(time.time()))
print("Local current time :", localtime)

# local time to UTC
# 2019-11-24 20:56:14, 1574600174
# timestamp = 1574600174

dt = datetime(2019, 11, 24, 20, 56, 14)
seconds_offset = time.timezone if (time.localtime().tm_isdst == 0) else time.altzone
print((dt+timedelta(seconds=seconds_offset)).timestamp())

print(arrow.utcnow().timestamp)
