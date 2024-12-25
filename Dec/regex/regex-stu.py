"""
匹配邮箱有效地址
exmple:example@example.com、user.name_123@domain.co、first-last@domain.org
work_eamil: rgdeng.work@outlook.com
思路： @之前必须有字符，@之后必须有字符，@之后必须有.
"""


"""
^[a-zA-Z0-9._%+-]+
^开头的符号或字符串，+号表示出现一次或多次。@分隔用户名和域名
@[a-zA-Z0-9.-]+
匹配域名部分，+号表示出现一次或多次。\.匹配.
\.[a-zA-Z]{2,}$
匹配域名的顶级域名，[a-zA-Z]{2,}表示至少两个字母的顶级域名,$表示匹配字符串的结尾
"""
import re
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None