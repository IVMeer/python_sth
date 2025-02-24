from cvat_sdk import Client

client = Client(url="http://192.168.30.245:8080/")
client.login('test', 'test1231')

"""
1.进入文件夹，上传文件名称后缀为scanning的文件夹
2.里面分为1-3个文件夹
3.上传完后，返回到anti-thief-oss路径，然后日期加一天，继续上述操作。
ps:应该入口处写好日期，按照所写日期上传其中的文件夹
文件总路径为：\\192.168.30.17\video\anti-thief-oss\
进入的日期文件路径为：\\192.168.30.17\video\anti-thief-oss\20241115或\\192.168.30.17\video\anti-thief-oss\20241116
创建任务和上传或许应该放在一个循环里
"""

# 创建任务名
"""
"""
task = client.tasks.create(name = '20241115-05-1')

# 上传文件
"""
遍历文件夹上传
"""
task.upload_data([
    "Z:\\anti-thief-oss\\20241115\\Q1400005_scanning\\1"
])