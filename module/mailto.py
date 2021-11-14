import smtplib
from email.mime.text import MIMEText
import sys
# 设置服务器所需信息
# SMTP服务器地址
mail_host = 'smtp.ym.163.com'  
# 用户名
mail_user = 'mailer@pixelwine.com.cn'  
# 密码(部分邮箱为授权码) 
mail_pass = 'pythonmailer'   
# 邮件发送方邮箱地址
sender = 'mailer@pixelwine.com.cn'  
# 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
receivers = [sys.argv[1]]  
# Email 标题
emailTitle = 'emailTitle'
# HTML 文件
htmlFilename = 'emailContent.html'
# 设置email信息
# 读HTML文件
with open(htmlFilename,'r') as f:
    content = f.read()
# 邮件内容设置
message = MIMEText(content,'html','utf-8')
# 邮件主题       
message['Subject'] = emailTitle
# 发送方信息
message['From'] = sender 
# 接受方信息     
message['To'] = receivers[0]  

# 登录SMTP服务器并发送邮件
try:
    smtpObj = smtplib.SMTP() 
    # 连接到服务器
    smtpObj.connect(mail_host,25)
    # 登录到服务器
    smtpObj.login(mail_user,mail_pass) 
    # 发送
    smtpObj.sendmail(sender,receivers,message.as_string()) 
    # 退出
    smtpObj.quit() 
    print('success')
except smtplib.SMTPException as e:
    print('error',e) # 打印错误
