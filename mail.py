import smtplib

smtp_obj = smtplib.SMTP('smtp.gmail.com',587)
type(smtp_obj)
smtp_obj.ehlo()
smtp_obj.starttls()
smtp_obj.login('送信元アドレス', 'パスワード',)
smtp_obj.sendmail('送信先1','送信先メアド2','Subject:hello\nhello,world!')
smtp_obj.quit()
