#!/usr/bin/env python
# coding:utf8
import re

import chardet
import requests

__author__ = 'xiamao'
__time__ = '2019/1/14 上午9:46'

"""
the main function, scrape emails of the domain from 2 palces:
the official website
the search engine
"""
ENGINE_DICT = {'baidu': 'http://www.baidu.com/search/s?wd="%40{word}"&pn={counter}',
               'bing': 'http://www.bing.com/search?q=%40{word}&count=50&first={counter}',
               'ask': ''}


def check_coding(req):
    try:
        result = chardet.detect(req.content)
        if result.get('confidence') > 0.9:
            html = req.content.decode(result.get('encoding'))
            return html
    except Exception as e:
        print str(e)
    if req.encoding == 'ISO-8859-1':
        encodings = requests.utils.get_encodings_from_content(req.text)
        if encodings:
            encoding = encodings[0]
        else:
            encoding = req.apparent_encoding
        # encode_content = req.content.decode(encoding, 'replace').encode('utf-8', 'replace')
        encode_content = req.content.decode(encoding, 'replace')
        return encode_content
    else:
        # req.encoding="utf-8"
        req.encoding = req.encoding
        return req.text


def crawl_official_website(domain):
    """
    用来爬取指定域名的官网上的所有信息。。目前是邮箱
    :param domain:
    :return:
    """
    pass


def crawl_search_engine(domain, engine):
    """
    爬取指定搜索引擎的有关域名的邮箱
    :param domain:
    :param engine:
    :return:
    """
    if engine == 'all':
        # 需要遍历所有支持的搜索引擎
        pass
    else:
        base_url = ENGINE_DICT.get(engine)
        url = base_url.format(word=domain, counter=10)
        resp = requests.get(url)
        return check_coding(resp)


def scrape(domain, engine):
    return extract(crawl_search_engine(domain, engine), domain)


def extract(html, base_str):
    """
    负责将html中所有符合的邮箱进行解析，可以增加base字符串
    :param html:
    :param base_str:
    :return:
    """
    for e in '''<KW> </KW> </a> <b> </b> </div> <em> </em> <p> </span>
                        <strong> </strong> <title> <wbr> </wbr>'''.split():
        html = html.replace(e, '')
    for e in '%2f %3a %3A %3C %3D & / : ; < = > \\'.split():
        html = html.replace(e, ' ')
    reg_emails = re.compile(
        '[a-zA-Z0-9.\-_+#~!$&\',;=:]+' +
        '@' +
        '[a-zA-Z0-9.-]*' + base_str)
    return reg_emails.findall(html)


if __name__ == '__main__':
    print scrape('bupt.edu.cn', 'bing')
