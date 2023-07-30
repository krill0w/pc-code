number = 0
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

while True:
    email = ''
    password = ''
    send_to_email = ''
    subject = 'Number ' + str(number) # The subject line
    message = 'poo'
    heheMessage = 'hehe'

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = subject

 # Attach the message to the MIMEMultipart object
    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    text = msg.as_string() # You now need to convert the MIMEMultipart object to a string to send
    number = number + 1
    server.sendmail(email, send_to_email,text)
    if number == 69:
      server.sendmail(email, send_to_email,message)
      server.sendmail(email, send_to_email,heheMessage)
      print("hehe message done")
    server.quit()
    print("Done " + str(number))
