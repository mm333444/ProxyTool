# -*- coding:utf-8 -*-
import time
import math
from app.validate.base import base
from app.util.requests_help import requests_help


class request_web(base):
    _url = 'https://www.baidu.com'

    def run(self, http_type, ip, port):
        _request_handle = requests_help()
        _result = _request_handle.setProxy(http_type, ip, port).setHeader('current_time', str(time.time())).get(self._url, 10)

        if _result:
            speed = math.ceil(time.time() - float(_request_handle.getRequestHeader('current_time')))
            self.updateIpInfo(ip, is_success=1, speed=speed)
        else:
            self.updateIpInfo(ip, is_success=0)
