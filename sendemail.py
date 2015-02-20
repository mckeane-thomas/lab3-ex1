import smtplib

fromaddr = 'mckeane27@gmail.com'

toaddr = 'david@alteroo.com'

message = """From: From Person <mckeane27@gmail.com>

To: To Person <david@alteroo.com>

Subject: SMTP e-mail test

This is my test email

"""

messagetosend = message.format(

fromname,

fromaddr,

toname,

toaddr,

subject,

msg)

# Credentials (if needed)

username = 'mckeane27@gmail.com'

password = 'mckeane_87'

# The actual mail send

server = smtplib.SMTP('smtp.gmail.com:587')

server.starttls()

server.login(username,password)

server.sendmail(fromaddr, toaddrs, messagetosend)

server.quit()
