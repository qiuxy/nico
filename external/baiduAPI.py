__author__ = 'qiuxy'
import json
from urllib import request
from core.dict import key

MOBILENUMBER_URL = "http://apis.baidu.com/apistore/mobilenumber/mobilenumber?"


class baiduAPI:
    def mobilenumber(phone):
        url = MOBILENUMBER_URL + 'phone=' + phone
        req = request.Request(url)
        req.add_header("apikey", key.BAIDU_APIKEY)
        resp = request.urlopen(req)
        content = resp.read()
        if (content):
            # {"errNum":0,"retMsg":"success","retData":{"phone":"13512279010","prefix":"1351227","supplier":"\u79fb\u52a8","province":"\u5929\u6d25","city":"\u5929\u6d25","suit":"135\u5361"}}
            return json.loads(content.decode('utf-8'))
