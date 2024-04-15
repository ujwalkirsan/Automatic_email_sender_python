# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 14:42:29 2024

@author: ujwal
"""

import pandas as pd
from send_email import send_email
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime


SHEET_ID = "1XuHmlXTpq9KpIUguHRbYyTVS342Zer9SkVHXmtUtYWk"
SHEET_NAME = "Sheet1"
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"


def load_df(url):
    df = pd.read_csv(url)
    return df

def query_data_and_send_emails(df):
    
    email_counter = 0
    for _,row in df.iterrows():
        if(row["greater_than_75_percent"] == "no"):
            send_email(
                subject = f'Attendance Remainder (Roll No:{row["Roll_No"]})',
                
                name = row["name"],
                receiver_email=row["email"],
                percent=row["percentage_of_attendance"],
                invoice_no=row["Roll_No"],
                amount=row["present_at_working_day"],
                )
            email_counter += 1
    return f"Total Emails Sent: {email_counter}"        



# manually sending mail
"""df = load_df(URL)
result = query_data_and_send_emails(df)
print(result)
"""

# using schedule library
def job_function():
    print(f"Executing job_function at {datetime.now()}")
    df = load_df(URL)
    result = query_data_and_send_emails(df)
    print(result)
    print("Email sending completed........")
    print("Press any key to countinue..")

print("Scheduling started......")
scheduler = BackgroundScheduler(timezone = 'Asia/Kolkata')

scheduler.add_job(job_function,'cron',hour=16,minute=6)

scheduler.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    print("Scheduler stopped manually")    



# BY Flask server
"""
from flask import Flask
 
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
 
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    df = load_df(URL)
    result = query_data_and_send_emails(df)
    return result
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()
"""