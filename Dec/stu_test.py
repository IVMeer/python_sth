"""
try: except:语句捕获异常
"""

try:
    num = int(input("输入数字:"))
    print(f"你输入的数字是:{ num }")
except:
    print("你输入的不是数字")