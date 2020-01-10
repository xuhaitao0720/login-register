import os
from django.core.mail import send_mail,EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE']='mysite.settings'

if __name__=='__main__':

    subject,from_email,to='来自127.0.0.1:8000/login的测试邮件','xht0720@163.com','xht0720@163.com'
    text_content='欢迎访问127.0.0.1:8000/login,如果看到这个，说明您的邮件服务器没有提供HTML支持'
    html_content='欢迎访问<a href="http://127.0.0.1:8000/login" target=blank>127.0.0.1:8000/login</a>,这里是测试网站'
    msg=EmailMultiAlternatives(subject,text_content,from_email,[to])
    msg.attach_alternative(html_content,'text/html')
    msg.send()