import datetime as dt
import smtplib
import pandas
import random
import time
import os

email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")

today = (dt.datetime.now().month, dt.datetime.now().day)
data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
print("Checking...")
time.sleep(0.5)
if today in birthday_dict:
    print("Creating Letter...")
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter:
        txt = letter.read()
        txt = txt.replace("[NAME]", birthday_dict[today]["name"])
    time.sleep(0.5)
    print("Connecting...")
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        print("Starting TLS...")
        connection.starttls()
        print("Logging in...")
        connection.login(user=email, password=password)
        print("Sending...")
        connection.sendmail(
            from_addr=email,
            to_addrs=birthday_dict[today]["email"],
            msg="Subject:Happy Birthday\n\n"
                f"{txt}\n\n"
        )
    print("Done")
else:
    print("No Birthdays Today")