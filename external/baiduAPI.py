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
            return json.loads(content.decode('utf-8'))

    def mobilenumber_format(info, column):
        try:
            if '0' == column:
                return info["retData"]["phone"] + "," + info["retData"]["prefix"] + "," + info["retData"][
                    "supplier"] + "," + \
                       info["retData"]["province"] + "," + info["retData"]["city"] + "," + info["retData"]["suit"]
            data = ''
            if '1' in column:
                data = data + info["retData"]["phone"] + ','
            if '2' in column:
                data = data + info["retData"]["prefix"] + ','
            if '3' in column:
                data = data + info["retData"]["province"] + ','
            if '4' in column:
                data = data + info["retData"]["suit"] + ','
            if '5' in column:
                data = data + info["retData"]["city"] + ','
            if '6' in column:
                data = data + info["retData"]["supplier"] + ','
            return data[0:len(data) - 1]
        except:
            return 'error'
