# auto-public-net

[TOC]

##auto_ip 自动获取IP发送邮件
感谢http://blog.0x0.codes/2015/08/01/ipsender-email-by-python/
###环境需要python
代码是用3.7写的，理论上支持python2.7以上的版本

###请求获取公网IP的网站
```
'https://jsonip.com/'
'https://www.ip.cn/'
'https://www.ipip.net/'
'http://ip111.cn/'
```
###邮箱配置
```
host = 'smtp.***.com'
port = 465
sender = '***@***.***'
receiver = ['***@***.***',
            '***@***.***', 
            '***@***.***']
pwd = '***'  # Password
```
###默认执行时间
默认66秒执行一次，根据自己的需要修改

##ali_auto_ip 自动获取IP更新阿里云域名解析
感谢https://www.vincents.cn/2017/03/27/aliyun-ddns/
利用阿里云API，动态修改域名解析
需要安装阿里云的python SDK

    pip install aliyun-python-sdk-alidns

```
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
```

