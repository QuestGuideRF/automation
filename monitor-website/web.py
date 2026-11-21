import requests
from playsound import playsound
import smtplib
url =''
PORT =587
Your_Email ='пример@company.com'
Your_Password ='password'
req =requests .get (url ,timeout =1 )
req .raise_for_status ()
while True :
    if req .status_code !=200 :
        with smtplib .SMTP ('smtp.gmail.com',PORT )as send__mail :
            send__mail .starttls ()
            send__mail .login (Your_Email ,Your_Password )
            sub ='Ваш сайт не работает!'
            body ='Перезапустите сервер и убедитесь, что он работает.'
            message =f'Subject: {sub } \n\n {body }'
            send__mail .sendmail (Your_Email ,Your_Email ,message )
            print ("Письмо отправлено!")
        playsound ('volume_warning.wav')
        break
    else :
        continue