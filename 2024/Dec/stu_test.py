"""
1.uuid 生成
2.除了uuid 以外,生成唯一id的方式→ 时间戳+随机数

"""
import uuid
import time 
import random

# 生成uuid
my_uuid = uuid.uuid4()
# 打印uuid
print(my_uuid)

# 时间戳+随机数
unique_id = f"{int(time.time() * 1000)}_{random.randint(1000, 9999)}"
print(unique_id)
