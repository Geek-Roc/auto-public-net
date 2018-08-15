# auto-public-net

- [auto-public-net](#auto-public-net)
    - [auto_ip 自动获取IP发送邮件](#autoip-%E8%87%AA%E5%8A%A8%E8%8E%B7%E5%8F%96ip%E5%8F%91%E9%80%81%E9%82%AE%E4%BB%B6)
        - [环境需要python](#%E7%8E%AF%E5%A2%83%E9%9C%80%E8%A6%81python)
        - [请求获取公网IP的网站](#%E8%AF%B7%E6%B1%82%E8%8E%B7%E5%8F%96%E5%85%AC%E7%BD%91ip%E7%9A%84%E7%BD%91%E7%AB%99)
        - [邮箱配置](#%E9%82%AE%E7%AE%B1%E9%85%8D%E7%BD%AE)
        - [默认执行时间](#%E9%BB%98%E8%AE%A4%E6%89%A7%E8%A1%8C%E6%97%B6%E9%97%B4)
    - [ali_auto_ip 自动获取IP更新阿里云域名解析](#aliautoip-%E8%87%AA%E5%8A%A8%E8%8E%B7%E5%8F%96ip%E6%9B%B4%E6%96%B0%E9%98%BF%E9%87%8C%E4%BA%91%E5%9F%9F%E5%90%8D%E8%A7%A3%E6%9E%90)
        - [环境](#%E7%8E%AF%E5%A2%83)

## auto_ip 自动获取IP发送邮件
感谢http://blog.0x0.codes/2015/08/01/ipsender-email-by-python/
### 环境需要python
代码是用3.7写的

### 请求获取公网IP的网站
```
'https://jsonip.com/'
'https://www.ip.cn/'
'https://www.ipip.net/'
'http://ip111.cn/'
```
### 邮箱配置
```python
host = 'smtp.***.com'
port = 465
sender = '***@***.***'
receiver = ['***@***.***',
            '***@***.***', 
            '***@***.***']
pwd = '***'  # Password
```
### 默认执行时间
默认66秒执行一次，根据自己的需要修改

## ali_auto_ip 自动获取IP更新阿里云域名解析
感谢https://www.vincents.cn/2017/03/27/aliyun-ddns/
利用阿里云API，动态修改域名解析
需要安装阿里云的python SDK

### 环境

> pip install aliyun-python-sdk-alidns

```python
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

