from datetime import datetime
import pandas as pd
import smtplib as st

data = pd.read_csv("./Birthday Wisher/birthdays.csv")

month = data["month"]
day = data["day"]

today = datetime.now().day
this_month = datetime.now().month
