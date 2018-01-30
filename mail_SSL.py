import smtplib
from email.mime.text import MIMEText

smtp_obj = smtplib.SMTP('smtp.gmail.com',587)
type(smtp_obj)
smtp_obj.ehlo()
smtp_obj.login('メアド', 'パス')
smtp_obj.sendmail('送信先1','送信先2','Subject:hello.\nhello,world!')
smtp_obj.quit()
