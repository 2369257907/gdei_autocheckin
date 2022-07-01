#!/usr/bin/python
# -*- coding: gbk -*-
import time
import datetime
from selenium import webdriver
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from selenium.webdriver.chrome.options import Options
#driver = webdriver.Chrome(chrome_options=chrome_options)#请替换成你的驱动的决定路径

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')  # “–headless”参数是不用打开图形界面（浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败）
chrome_options.add_argument('blink-settings=imagesEnabled=false')
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome("/etc/yum.repos.d/chromedriver",chrome_options=chrome_options)#请替换成你的驱动的决定路径

driver.get('https://tb.gdei.edu.cn/system/main')
time.sleep(1)
 
username = "xxxx" # 请替换成你的用户名

password = "xxx" # 请替换成你的密码

 #采用xpath定位用户名、密码按钮，
driver.find_element_by_xpath('//*[@id="signupForm"]/input[1]').click() # 点击用户名输入框
driver.find_element_by_xpath('//*[@id="signupForm"]/input[1]').send_keys(username) # 自动敲入用户名
 
driver.find_element_by_xpath('//*[@id="signupForm"]/input[2]').click() # 点击密码输入框
driver.find_element_by_xpath('//*[@id="signupForm"]/input[2]').send_keys(password) # 自动敲入密码

#采用xpath定位登陆按钮，
driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()

driver.get('https://tb.gdei.edu.cn/index')
driver.get('https://tb.gdei.edu.cn/system/main')

#晨午检、一键打卡
driver.find_element_by_xpath('//h3[text()="一键晨午检"]/.././..').click()#点击晨午检按钮
driver.find_element_by_xpath('//*[@id="dk"]').click()  # 点击晨午检按钮


driver.close();
driver.quit()

#发送打卡成功信息到指定邮箱


host_server = 'smtp.qq.com'  #qq邮箱smtp服务器
sender_qq = 'xxxx@qq.com' #发件人邮箱
pwd = 'xxxxxx'    #smtp授权码
receiver = ['xxxx@qq.com' ]#收件人邮箱

date_p = datetime.datetime.now().date()
str_p = str(date_p)
mail_title =str_p+'linux自动打卡成功' #邮件标题
mail_content =  "【广东二师晨午检】您好，您今天的（健康打卡/晨午检）已自动打卡成功。" #邮件正文内容
# 初始化一个邮件主体
msg = MIMEMultipart()
msg["Subject"] = Header(mail_title,'utf-8')
msg["From"] = sender_qq
# msg["To"] = Header("测试邮箱",'utf-8')
msg['To'] = ";".join(receiver)
# 邮件正文内容
msg.attach(MIMEText(mail_content,'plain','utf-8'))



smtp = SMTP_SSL(host_server) # ssl登录

# login(user,password):
# user:登录邮箱的用户名。
# password：登录邮箱的密码，smtp授权码。
smtp.login(sender_qq,pwd)


smtp.sendmail(sender_qq,receiver,msg.as_string())

# quit():用于结束SMTP会话。
smtp.quit()
