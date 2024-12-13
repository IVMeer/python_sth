"""
CVAT提供了基于REST API 的文件上传接口，


上传网址: http://192.168.30.245:8080/tasks/create?projectId=63


"""

import requests
base_url = "http://192.168.30.245:8080"
projectId = 63
upload_url = f"{base_url}/tasks/create?projectId={projectId}"

"""
    http://192.168.30.245:8080/api/tasks/1006/data?org=antithiefoss
    http://192.168.30.245:8080/api/labels?project_id=63&org=antithiefoss&page_size=500&page=1

"""
