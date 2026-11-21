import smtplib
from email .message import EmailMessage
PORT =587
Your_Email ='пример@company.com'
Your_Password ='password'
receiver =input ("Лицо, получающее электронное письмо: ")
subject =input ("Тема сообщения: ")
content =input ("Содержание сообщения: ")
with smtplib .SMTP ('smtp.gmail.com',PORT )as send__mail :
    send__mail .starttls ()
    send__mail .login (Your_Email ,Your_Password )
    message =EmailMessage ()
    message ['From']=Your_Email
    message ['To']=receiver
    message ['subject']=subject
    message .set_content (content )
    send__mail .send_message (message )
    print ("Письмо отправлено!")