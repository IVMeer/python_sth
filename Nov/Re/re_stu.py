import re

text = "my phone number is 138123456789"
pattern = r'1[3-9]\d{9}'
match = re.search(pattern, text)
if match:
    print(f'匹配到电话号码:{match.group()}')
