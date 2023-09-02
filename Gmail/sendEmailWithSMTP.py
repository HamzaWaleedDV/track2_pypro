import smtplib
# ictaqtqzorbghmqd
sender_email = "hamzanasr412@gmail.com"
rec_email = "hamzawaleed061@gmail.com"
password = input('enter your password: ')
message = "Subject: Python Message.\nHello, This message sent using Python"

for i in range(100):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    print("Login success")
    server.sendmail(sender_email, rec_email, message)
    message += '.'

    print("Email has been sent to ", rec_email)
    server.quit()