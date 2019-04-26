import urllib2
import json

headers = {'Content-Type': 'application/json; charset=utf-8'}

XXX_HOST = "http://xxx.xxx.com/xxx-app/"

# post请求，json格式数据


def post_json(url, header, request_data):
    req = urllib2.Request(url, request_data, header)
    page = urllib2.urlopen(req)
    res = page.read()
    page.close()
    return res


YYY_HOST = "http://yyy.yyy.com/yyy-app/"

# get请求


def get_(param1, param2):
    url = YYY_HOST + "yyyy/yyyy?param1=" + \
        str(param1) + "&param2=" + str(param2) + "&param3=VIP"
    req = urllib2.Request(url)
    page = urllib2.urlopen(req, timeout=5000)
    res = page.read()
    page.close()
    return json.loads(res)["data"]