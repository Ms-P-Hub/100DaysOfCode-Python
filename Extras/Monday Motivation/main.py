import smtplib
from datetime import datetime
import random

if datetime.now().weekday() == 0:
    with open("./Extras/Monday Motivation/quotes.txt") as file:
        data = file.readlines()
        quote = random.choice(data)
        
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="",password="")
        connection.sendmail(from_addr="", to_addrs="", msg=f"Subject:Monday Motivation\n\n{quote}\nSent from python code.\n\nKind Regards\nGugu P. Mokwena")