from datetime import datetime,timedelta
from pathlib import Path
from cvat_sdk import Client

import datetime
# 获取当前时间
today = datetime.date.today()
print(today)
now = datetime.datetime.now()
print(now)

# 自定义日期和时间
custom_date = datetime.date(2024,12,11)
print(custom_date)

custom_datetime = datetime.datetime(2024,12,11,14,30,0)
print(custom_datetime)