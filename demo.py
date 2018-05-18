import requests

#请求接口
def resp_get(url):
    response = requests.get(url)
    return response

