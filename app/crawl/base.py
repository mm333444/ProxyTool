# -*- coding:utf-8 -*-
import time
from app.mongo_model.ip import ip
from app.util.requests_help import requests_help


class base(object):
    ''' 抓取基类 '''
    max_page = 0
    black_list = [
        '218.4.101.130',
    ]

    def __init__(self):
        pass

    def _save(self, data):
        ''' 保存数据到mongo '''
        ip_list = [value.get('ip')for value in data]
        ip_list = ip().listByIp(ip_list)

        if ip_list:
            data = [_data for _data in data if _data.get('ip') not in ip_list and _data.get('ip') not in self.black_list]

        if data:
            ip().addMany(data)

    def _crawl_single(self, url):
        ''' 抓取单个页面'''
        _body = requests_help().get(url)

        if _body:
            _data = self._parse_html(_body)

        self._save(_data)

    def _parse_html(self, body):
        pass

    def _crawl_page(self, url):
        ''' 分页抓取 '''
        for i in range(0, self.max_page):
            _url = url % (int(i) + 1)
            self._crawl_single(_url)
            time.sleep(5)
