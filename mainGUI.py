from tkinter import *
import time
import smtplib
from email.mime.text import MIMEText
import sys
LOG_LINE_NUM = 0

class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name


    # 设置窗口
    def set_init_window(self):
        self.init_window_name.title("Wine Mailer v1.0")           # 窗口名
        # self.init_window_name.geometry('320x160+10+10')                         # 290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window_name.geometry('1068x681+10+10')
        self.init_window_name["bg"] = "Azure"                                    # 窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        # self.init_window_name.attributes("-alpha",0.9)                          # 虚化，值越小虚化程度越高
        # 标签
        self.init_data_label = Label(self.init_window_name, text="收件人邮件地址")
        self.init_data_label.grid(row=0, column=0)
        self.title_data_label = Label(self.init_window_name, text="邮件标题")
        self.title_data_label.grid(row=3, column=0)
        self.result_data_label = Label(self.init_window_name, text="邮件内容（支持 PlainText 及 HTML）")
        self.result_data_label.grid(row=0, column=12)
        self.log_label = Label(self.init_window_name, text="日志")
        self.log_label.grid(row=12, column=0)
        # 文本框
        self.init_data_Text = Text(self.init_window_name, width=50, height=5)  # 对方邮件地址输入框
        self.init_data_Text.grid(row=1, column=0, rowspan=2, columnspan=3)
        self.title_data_Text = Text(self.init_window_name, width=50, height=5)  # 邮件标题输入框
        self.title_data_Text.grid(row=5, column=0, rowspan=2, columnspan=3)
        self.content_data_Text = Text(self.init_window_name, width=70, height=49) # 邮件内容输入框
        self.content_data_Text.grid(row=1, column=12, rowspan=15, columnspan=10)
        self.log_data_Text = Text(self.init_window_name, width=66, height=9)  # 日志框
        self.log_data_Text.grid(row=13, column=0, columnspan=10)
        # 按钮
        self.mailto_button = Button(self.init_window_name, text="发送", bg="lightblue", width=10,command=self.mailto)  #  调用内部方法  加()为直接调用
        self.mailto_button.grid(row=1, column=11)


    # 功能函数
    def mailto(self):
        mail_host = 'smtp.ym.163.com'  
        # 用户名
        mail_user = 'mailer@pixelwine.com.cn'  
        # 密码(部分邮箱为授权码) 
        mail_pass = '***********************'   
        # 邮件发送方邮箱地址
        sender = 'Wine Mailer<mailer@pixelwine.com.cn>'  
        # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
        receivers = self.init_data_Text.get(1.0,END).strip().replace("\n","").split(",")
        # Email 标题
        emailTitle = self.title_data_Text.get(1.0,END).strip()
        # # HTML 文件
        # htmlFilename = 'emailContent.html'
        # # 设置email信息
        # # 读HTML文件
        # with open(htmlFilename,'r') as f:
        #     content = f.read()
        # 邮件内容设置
        content = self.content_data_Text.get(1.0,END).strip().replace("\n","") + "<br><br><br><footer>Sent by Wine Mailer~ <br>Welcome to try this new mailer~<br>It is <a href=\"https://github.com/PixelWine/WineMailer\">open source</a><br>and you can download the latest release on <a href=\"https://blog.pixelwine.top/posts/111#download\">this page</a>.</footer>"
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
            self.write_log_to_Text("[INFO] function mailto success")
        except smtplib.SMTPException as e:
            self.write_log_to_Text("[FATAL] function mailto error")


    # 获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return current_time


    # 日志动态打印
    def write_log_to_Text(self,logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) +" " + str(logmsg) + "\n"      # 换行
        if LOG_LINE_NUM <= 7:
            self.log_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0,2.0)
            self.log_data_Text.insert(END, logmsg_in)


def gui_start():
    init_window = Tk()              # 实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()          # 父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示
gui_start()
