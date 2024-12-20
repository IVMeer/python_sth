"""
1.uuid 生成
2.
"""
import uuid
import time 
import random

# 生成uuid
my_uuid = uuid.uuid4()
print(my_uuid)


unique_id = f"{int(time.time() * 1000)}_{random.randint(1000, 9999)}"
print(unique_id)