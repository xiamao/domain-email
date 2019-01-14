#!/usr/bin/env python
# coding:utf8
__author__ = 'xiamao'
__time__ = '2019/1/14 上午11:22'
import re


def extract_email(html, domain):
    pass


def extract_url(target_str, html):
    pass


def extract_website_url(website_html, layers):
    pass


def extract_keywords(website_html):
    ks = re.findall('<meta name="keywords" content="(.*?)">', website_html)
    ks = re.split(',，', ks[0]) if ks else []
    return ks


def extract_desc(html):
    desc = re.findall('<meta name="description"\s*\n*content="(.*?)">', html)
    pass


def extract_phone(html):
    phones = re.findall('^(?:\+?86)?1(?:3\d{3}|5[^4\D]\d{2}|8\d{3}|7(?:[01356789]\d{2}|4'
                        '(?:0\d|1[0-2]|9\d))|9[189]\d{2}|6[567]\d{2}|4(?:[14]0\d{3}|[68]'
                        '\d{4}|[579]\d{2}))\d{6}$', html)

    return phones


if __name__ == '__main__':
    import requests
    resp = requests.get('https://www.baidu.com')
    print extract_phone(resp.content)