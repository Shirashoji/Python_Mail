import smtplib

smtp_obj = smtplib.SMTP('smtp.gmail.com','587')
smtp_obj.ehlo()
smtp_obj.starttls()
smtp_obj.login('送信元メアド','パスワード')
smtp_obj.sendmail('送信先メアド','送信先2','Subject: hello \n hello,world!')
{}
smtp_obj.quit()
