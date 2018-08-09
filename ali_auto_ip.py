#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from urllib import request
from collections import Counter
import re
import json

from aliyunsdkcore import client
from aliyunsdkalidns.request.v20150109 import DescribeDomainRecordsRequest
from aliyunsdkalidns.request.v20150109 import DescribeDomainRecordInfoRequest
from aliyunsdkalidns.request.v20150109 import UpdateDomainRecordRequest

"""
利用阿里云API，动态修改域名解析
需要安装阿里云的python SDK
pip install aliyun-python-sdk-alidns
"""
# 阿里云 Access Key ID
access_key_id = "***"
# 阿里云 Access Key Secret
access_key_secret = "***"
# 阿里云 一级域名
ali_domain = '***.***'
# 阿里云 主机记录
ali_domain_rr = '***'
# 返回内容格式
ali_format = 'json'
# 记录类型, DDNS填写A记录
ali_type = 'A'
# 解析记录有效生存时间TTL,单位:秒  阿里云解析免费版最少600  
ali_ttl = '600'             

"""
获取域名的解析信息
"""
def check_records(dns_domain):
    clt = client.AcsClient(access_key_id, access_key_secret, 'cn-hangzhou')
    request = DescribeDomainRecordsRequest.DescribeDomainRecordsRequest()
    request.set_DomainName(dns_domain)
    request.set_accept_format(ali_format)
    request.set_RRKeyWord(ali_domain_rr)
    result = clt.do_action(request)
    result = json.loads(result)
    return result


"""
根据域名解析记录ID查询上一次的IP记录
"""
def get_old_ip(record_id):
    clt = client.AcsClient(access_key_id, access_key_secret, 'cn-hangzhou')
    request = DescribeDomainRecordInfoRequest.DescribeDomainRecordInfoRequest()
    request.set_RecordId(record_id)
    request.set_accept_format(ali_format)
    result = clt.do_action(request)
    result = json.loads(result)
    result = result['Value']
    return result


"""
更新阿里云域名解析记录信息
"""
def update_dns(dns_rr, dns_type, dns_value, dns_record_id, dns_ttl, dns_format):
    clt = client.AcsClient(access_key_id, access_key_secret, 'cn-hangzhou')
    request = UpdateDomainRecordRequest.UpdateDomainRecordRequest()
    request.set_RR(dns_rr)
    request.set_Type(dns_type)
    request.set_Value(dns_value)
    request.set_RecordId(dns_record_id)
    request.set_TTL(dns_ttl)
    request.set_accept_format(dns_format)
    result = clt.do_action(request)
    return result


"""
通过 https://jsonip.com/
    https://www.ip.cn/
    https://www.ipip.net/
    http://ip111.cn/ 获取当前主机的外网IP
"""


def get_my_publick_ip():
    get_ip_urls = ['https://jsonip.com/',
                   'https://www.ip.cn/',
                   'https://www.ipip.net/',
                   'http://ip111.cn/']
    # 模拟浏览器访问，避免被网站屏蔽
    header = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
    }
    get_ip_values = []
    for url in get_ip_urls:
        try:
            req = request.Request(url, headers=header)
            html = request.urlopen(req).read()
            print('request:' + url)
            content = html.decode('utf-8')  # utf-8解码
            pattern = re.compile(
                r'((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))', re.M | re.I)
            ipAddress = pattern.search(content).group(0)
        except Exception as e:
            print('error:' + str(e))
        else:
            get_ip_values.append(ipAddress)
            print('success:' + url + ":" + ipAddress)
    get_ip_values_counter = Counter(get_ip_values)
    if len(get_ip_values_counter) > 0:
        get_ip_value = get_ip_values_counter.most_common()[0][0]
        return get_ip_value


if __name__ == "__main__":
    # # 之前的解析记录
    old_ip = ""
    record_id = ""
    dns_records = check_records(ali_domain)
    for record in dns_records['DomainRecords']['Record']:
        if record['Type'] == 'A' and record['RR'] == ali_domain_rr:
            record_id = record['RecordId']
            old_ip = record['Value']
            print("%s.%s value is %s" % (ali_domain_rr, ali_domain, old_ip))

    now_ip = get_my_publick_ip()
    print("now host ip is %s, dns ip is %s" % (now_ip, old_ip))

    if old_ip == now_ip:
        print('The specified value of parameter Value is the same as old')
    else:
        update_dns(ali_domain_rr, ali_type, now_ip, record_id, ali_ttl, ali_format)
        print('Now dns ip is the latest')

