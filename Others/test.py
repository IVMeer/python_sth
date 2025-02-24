import openai

# 设置APIKEY
openai.api_key = ''

# 请求模型
response = openai.completions.create(
    model = 'gpt-4',
    prop = ''
)