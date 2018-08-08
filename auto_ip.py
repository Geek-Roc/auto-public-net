#!/usr/local/bin/python3
# coding=utf-8

import smtplib
from email.mime.text import MIMEText
from urllib import request
from collections import Counter
import re
import time
import threading

textList = []
sendIPAddress = ''


def sendIP(content):
    # config
    host = 'smtp.***.com'
    port = 465
    sender = '***@***.***'
    receiver = ['***@***.***',
                '***@***.***', 
                '***@***.***']
    pwd = '***'  # Password
    # core
    msg = MIMEText(content, _subtype='plain', _charset='utf-8')
    msg['subject'] = 'IP changed. Please handle it quickly'
    msg['from'] = sender
    msg['to'] = ",".join(receiver)

    try:
        hero = smtplib.SMTP_SSL(host=host, port=port)
        hero.login(sender, pwd)
        hero.sendmail(sender, receiver, msg.as_string())
    except Exception as e:
        print('error:', str(e))
    else:
        print('IP is sended successly.')


def getIP():
    urls = ['https://jsonip.com/',
            'https://www.ip.cn/',
            'https://www.ipip.net/',
            'http://ip111.cn/']
    #Simulate browser access to avoid being blocked by the site
    header = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
    }
    ips = []
    for url in urls:
        try:
            req = request.Request(url, headers=header)
            html = request.urlopen(req).read()
            print('request:' + url)
            content = html.decode('utf-8')  # utf-8 decode
            pattern = re.compile(
                r'((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))', re.M | re.I)
            ipAddress = pattern.search(content).group(0)
        except Exception as e:
            textList.append('error:' + str(e))
            print('error:' + str(e))
        else:
            textList.append(url)
            textList.append(ipAddress)
            ips.append(ipAddress)
            print('success:' + url + ":" + ipAddress)
    ipsCounter = Counter(ips)
    if len(ipsCounter) > 0:
        ip = ipsCounter.most_common()[0][0]
        return ip


def checkIP():
    global sendIPAddress
    print('Checking...')
    nowIp = getIP()

    if sendIPAddress != nowIp:
        sendIPAddress = nowIp
        print('IP changed '+nowIp)
        textList.insert(0, sendIPAddress)
        nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        textList.insert(1, nowtime)
        content = '\n'.join(textList)
        sendIP(content)
    else:
        print('IP not change')

    textList.clear()
    t = threading.Timer(66.0, checkIP)
    t.start()


if __name__ == "__main__":
    print("start")
    sendIPAddress = getIP()
    textList.insert(0, sendIPAddress)
    nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    textList.insert(1, nowtime)
    content = '\n'.join(textList)
    sendIP(content)
    textList.clear()

    t = threading.Timer(66.0, checkIP)
    t.start()
