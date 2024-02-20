from datetime import datetime
import pandas as pd
import smtplib
import random

data = pd.read_csv("./Birthday Wisher/birthdays.csv")

month = data.month
day = data.day
name = data.name
email = data.email.item()

today = datetime.now().day
this_month = datetime.now().month

if today == day.item() and this_month == month.item():
    with open(
        f"./Birthday Wisher/letter_templates/letter_{random.randint(1,3)}.txt"
    ) as file:
        content = file.read()
        if "[NAME]" in content:
            content = content.replace("[NAME]", name.item().title())
            
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user="", password="")
    connection.sendmail(from_addr="", to_addrs=email, msg=f"subject:Happy Birthday\n\n{content}")
