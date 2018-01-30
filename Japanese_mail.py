import smtplib
from email.mime.text import MIMEText
from email.header import Header

charset = 'iso-2022-jp'

msg = MIMEText('私の名前はSSJ','plain', charset)
msg['Subject'] = Header('こんにちは'.encode(charset), charset)

smtp_obj = smtplib.SMTP('smtp.gmail.com',587)
smtp_obj.ehlo()
smtp_obj.starttls()
smtp_obj.login('送信元のメールアドレス', '送信元のパスワード')
for range(5):
    smtp_obj.sendmail('送信先のメアド1', '送信先のメアド2', msg.as_string())
smtp_obj.quit()
