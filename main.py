import os
import smtplib

MY_EMAIL = "rahulparmar1978@gmail.com"
MY_PASSWORD = os.environ["MY_PASSWORD"]

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(
        user=MY_EMAIL,
        password=MY_PASSWORD
    )
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg=f"Subject:Happy Birthday\n\n...to you!"
    )
