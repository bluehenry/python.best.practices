import schedule
import time
import datetime

def get_time():
    print(datetime.datetime.now())



schedule.every(1).minutes.do(get_time)
get_time()
while True:
    schedule.run_pending()
    time.sleep(1*60)