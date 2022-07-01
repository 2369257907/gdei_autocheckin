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
#driver = webdriver.Chrome(chrome_options=chrome_options)#���滻����������ľ���·��

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')  # ���Cheadless�������ǲ��ô�ͼ�ν��棨��������ṩ���ӻ�ҳ��. linux�����ϵͳ��֧�ֿ��ӻ���������������ʧ�ܣ�
chrome_options.add_argument('blink-settings=imagesEnabled=false')
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome("/etc/yum.repos.d/chromedriver",chrome_options=chrome_options)#���滻����������ľ���·��

driver.get('https://tb.gdei.edu.cn/system/main')
time.sleep(1)
 
username = "xxxx" # ���滻������û���

password = "xxx" # ���滻���������

 #����xpath��λ�û��������밴ť��
driver.find_element_by_xpath('//*[@id="signupForm"]/input[1]').click() # ����û��������
driver.find_element_by_xpath('//*[@id="signupForm"]/input[1]').send_keys(username) # �Զ������û���
 
driver.find_element_by_xpath('//*[@id="signupForm"]/input[2]').click() # ������������
driver.find_element_by_xpath('//*[@id="signupForm"]/input[2]').send_keys(password) # �Զ���������

#����xpath��λ��½��ť��
driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()

driver.get('https://tb.gdei.edu.cn/index')
driver.get('https://tb.gdei.edu.cn/system/main')

#����졢һ����
driver.find_element_by_xpath('//h3[text()="һ�������"]/.././..').click()#�������찴ť
driver.find_element_by_xpath('//*[@id="dk"]').click()  # �������찴ť


driver.close();
driver.quit()

#���ʹ򿨳ɹ���Ϣ��ָ������


host_server = 'smtp.qq.com'  #qq����smtp������
sender_qq = 'xxxx@qq.com' #����������
pwd = 'xxxxxx'    #smtp��Ȩ��
receiver = ['xxxx@qq.com' ]#�ռ�������

date_p = datetime.datetime.now().date()
str_p = str(date_p)
mail_title =str_p+'linux�Զ��򿨳ɹ�' #�ʼ�����
mail_content =  "���㶫��ʦ����졿���ã�������ģ�������/����죩���Զ��򿨳ɹ���" #�ʼ���������
# ��ʼ��һ���ʼ�����
msg = MIMEMultipart()
msg["Subject"] = Header(mail_title,'utf-8')
msg["From"] = sender_qq
# msg["To"] = Header("��������",'utf-8')
msg['To'] = ";".join(receiver)
# �ʼ���������
msg.attach(MIMEText(mail_content,'plain','utf-8'))



smtp = SMTP_SSL(host_server) # ssl��¼

# login(user,password):
# user:��¼������û�����
# password����¼��������룬smtp��Ȩ�롣
smtp.login(sender_qq,pwd)


smtp.sendmail(sender_qq,receiver,msg.as_string())

# quit():���ڽ���SMTP�Ự��
smtp.quit()
