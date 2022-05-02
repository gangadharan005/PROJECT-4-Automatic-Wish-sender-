import datetime as dt
import pandas as pd
from random import choice,randint
import smtplib

my_email = 's.gangadharan07@gmail.com'
password = 'g123456.'
read_file = pd.read_excel (r'C:\Users\GANGADHARAN\Documents\Python(Pycharm)\birthdaywishes.xlsx')
read_file.to_csv(r'C:\Users\GANGADHARAN\Documents\Python(Pycharm)\sample.csv', index = None, header=True)

def send_email(name,email):
    print(f"name={name},email={email}")
    random_letter_numbers = randint(1,3)
    random_letter = f"letter_templates/letter_{random_letter_numbers}.txt"
    with open("letter_templates/letter_1.txt") as file:
        content = file.read()
        content = content.replace("[NAME]",name)

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email, to_addrs=email, msg=f"Subject:Happy Birthday!\n\n{content}")
        print("mail sent successfully")

now = dt.datetime.now()
month = now.month
day = now.day

birthdays = pd.read_csv("sample.csv")

for index,row in birthdays.iterrows():
    print(f"Name={row['name']},Email={row['email']},Day={row['day']},Month={row['month']}")

    if day == row['day'] and month == row['month']:
        send_email(name=row['name'],email=row['email'])
    else:
        print("Not available day and month")



