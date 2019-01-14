#!/usr/bin/env python
# coding:utf8
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
        print resp.content

    pass


def scrape(domain, engine):
    crawl_search_engine(domain, engine)


if __name__ == '__main__':
    scrape('baidu.com', 'baidu')
