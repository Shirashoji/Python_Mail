import smtplib
from email.mime.text import MIMEText

if __name__ == '__main__':
    to_addr = '送信先メアド'
    from_addr = '送信元'
    mail_id = 'fihbhgzxntcnwyan'
    mail_pass = 'パスワード'

    message = MIMEText('Hello')
    message['Subject'] = 'Hello,world!!'
    message['From'] = from_addr
    message['To'] = to_addr

smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
smtp_obj.ehlo()
smtp_obj.starttls()
smtp_obj.login(mail_id, mail_pass)
smtp_obj.sendmail(from_addr, to_addr, message.as_string())
smtp_obj.quit()
