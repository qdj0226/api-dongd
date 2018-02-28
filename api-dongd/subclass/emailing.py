#-*- coding:utf-8 -*-
__author__ = "dongd"

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import configparser,os,time



class MyEmail():
    '''封装email类'''
    def __init__(self,email_config):
        '''
        初始化email的配置信息，读取配置文件中的信息
        :param email_config: email配置文件
        '''
        config = configparser.ConfigParser()
        config.read(email_config,encoding="utf-8")

        self.login_user = config.get('EMAIL', 'login_user')
        self.login_pwd = config.get('EMAIL', 'login_pwd')
        self.from_addr = config.get('EMAIL', 'from_addr')
        self.to_addrs = config.get('EMAIL', 'to_addrs')
        self.host = config.get('EMAIL', 'host')
        self.port = config.get('EMAIL', 'port')
        date = time.strftime("%Y-%m-%d")
        self.title = config.get('EMAIL', 'title')
        self.title = "".join([self.title,date])
        self.encrypt = config.get('EMAIL', 'encrypt')
        self.host = config.get('EMAIL', 'host')
        self.port = int(config.get('EMAIL', 'port'))
        if int(self.encrypt) == 1:
                self.smtp = smtplib.SMTP_SSL(self.host,self.port)
        else:
            self.smtp = smtplib.SMTP()

    def connent(self):
        '''连接邮箱服务器'''
        self.smtp.connect(self.host, self.port)

    def loggin(self):
        '''登录邮箱'''
        self.smtp.login(self.login_pwd, self.login_pwd)

    def send_email(self,accessory,):
        '''发送邮件'''
        msg = MIMEMultipart()
        msg["Subject"] = self.title
        msg["From"] = self.from_addr
        msg["To"] = self.to_addrs
        msg['Date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
        att = MIMEText(open(accessory,"rb").read(),"base64","utf-8")
        # filename = (time.strftime("%Y-%m-%d"))+"测试报告.html"
        filename = os.path.basename(accessory)
        att["Content-Type"] = 'application/octet-stream'
        att.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', filename))
        txt = MIMEText("这是测试报告的邮件，详情见附件", 'plain', 'gb2312')
        msg.attach(txt)
        msg.attach(att)
        server = smtplib.SMTP_SSL(self.host,self.port)
        server.login(self.login_user,self.login_pwd)
        server.sendmail(self.from_addr,self.to_addrs,msg.as_string())
        server.quit()

if __name__ == '__main__':
    configpath = os.path.abspath(os.path.join(os.path.dirname(__file__),"../","config","emailconfig.ini"))
    filepath = os.path.abspath(os.path.join(os.path.dirname(__file__),"../","testreports","lilin_app2018-0227 162803.html"))
    my = MyEmail(configpath)
    my.send_email(filepath)
