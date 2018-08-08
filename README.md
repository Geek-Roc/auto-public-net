# auto-public-net
自动获取公网IP地址，发送到指定邮箱

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


