# 1. Send automated email remainder to students

This is a Python script for automating the sending of email reminders based on data from a Google Sheets document. It uses the pandas library to read data from the Google Sheets document, and the apscheduler library to schedule and execute email sending tasks periodically.

# 2. Prerequisites

Before running the script, ensure you have the following installed:

Python 3+ version
Required Python packages (pandas, apscheduler)
An email account (e.g., Gmail, Outlook) for sending emails
Access to a Google Sheets document with the required data

# 4. Setup

1. navigate the project directory:
`cd automated_email_reminder`

2. Install the required Python packages:
`pip install -r requirements.txt`

3. Set up environments variables:
Create a '.env' file in the project directory and insert the following variables:
ex:-
```.env
EMAIL=your_email@example.com
PASSWORD=your_email_password
```
Replace your_email@example.com and your_email_password
with your email credentials.
```python
#you have to change this also in send_mail.py file
# EMAIL_SERVER = "smtp-mail.outlook.com" # for outlook server
EMAIL_SERVER = "smtp.gmail.com" # for gmail server
```
NOTE :- If you are using gmail.com as your email server then make a new app-specific password in app passwords in google accounts and then give any name to it and then it will show you a 16 digit alphabets password then you have to paste this password as the email password in your env file
(for the above method you need to verify that your two factor authentication of the google is on otherwise the app password will not show to you)
link for creating app password :- https://accounts.google.com/v3/signin/challenge/pwd?TL=AEzbmxx-_vJrRHvDX_9gJcYIOdjDSNqm_ouMGFF-V_ZqNSNm82s-dK3opeU2dOJk&cid=2&continue=https%3A%2F%2Fmyaccount.google.com%2Fapppasswords&flowName=GlifWebSignIn&followup=https%3A%2F%2Fmyaccount.google.com%2Fapppasswords&ifkv=ARZ0qKLF45IQWgmvdZt3EQ-xIAEwO0Pr58My2H5tl3zfqL7fRLVal-salXWYanmi2RvEBFA3L-NNGg&osid=1&rart=ANgoxcdi_d-pr6T3OiSThx18wxtz0y3EkcU2niNlA2hQBhoBr_KcxWhAmukCIB8bmgDVI1l_B96gm2vYehgu2SIIOPIqW_6_Grf-bo6zfWXDzKtE1c73bwE&rpbg=1&service=accountsettings&theme=mn

4. Configure Google Sheets access:

Obtain the Google Sheets document ID (SHEET_ID) and sheet name (SHEET_NAME) that contains the data you want to use.
Ensure the Google Sheets document is shared with the email address associated with the Google account you are using to access it.
Here SHEET_ID is = "1XuHmlXTpq9KpIUguHRbYyTVS342Zer9SkVHXmtUtYWk"
and SHEET_NAME is = "Sheet1"

I have attach the link of the google sheets where you can see the students data :-
https://docs.google.com/spreadsheets/d/1XuHmlXTpq9KpIUguHRbYyTVS342Zer9SkVHXmtUtYWk/edit#gid=0

# 5. Usage

1. If you want to only test the code then in send_email.py you have to write your_email_address@email.com
change the following code in send_email.py accordingly.
```python
if __name__ == "__main__":
    send_email(
        subject = "Attendance Remainder: 220150026", # your roll no
        name = "Ujwal Kirsan", # your name
        receiver_email="ujwalkirsan2003@gmail.com", #your_email_address@email.com
        percent="40%", # your percent
        roll_no="220150026", # your roll no
        classes="12", # no of classes attent
        attachments=["requirements.txt","IITG_logo.png"] # attachments
        
        )  
```
2. You can run the main.py script manually for do so you have to comment out the schedule time code in the main.py script as you can see in this below code:
```python
`# manually sending mail

df = load_df(URL)
result = query_data_and_send_emails(df)
print(result)

`# using schedule library (set time in which you want to send the mail)
`# comment this code in main.py
"""
def job_function():
    print(f"Executing job_function at {datetime.now()}")
    df = load_df(URL)
    result = query_data_and_send_emails(df)
    print(result)
    print("Email sending completed........")
    print("Press any key to countinue..")

print("Scheduling started......")
scheduler = BackgroundScheduler(timezone = 'Asia/Kolkata')

scheduler.add_job(job_function,'cron',hour=23,minute=6)

scheduler.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    print("Scheduler stopped manually")    

"""
```

3. You can run the main.py script at a schedule time to do so you have to comment out the manually method code in the main.py script as you can see in this below code:
```python
`# manually sending mail
`# comment this code
"""
df = load_df(URL)
result = query_data_and_send_emails(df)
print(result)

"""

`# using schedule library (set time in which you want to send the mail)
def job_function():
    print(f"Executing job_function at {datetime.now()}")
    df = load_df(URL)
    result = query_data_and_send_emails(df)
    print(result)
    print("Email sending completed........")
    print("Press any key to countinue..")

print("Scheduling started......")
scheduler = BackgroundScheduler(timezone = 'Asia/Kolkata')

scheduler.add_job(job_function,'cron',hour=23,minute=6) # change this time for your scheduling

scheduler.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    print("Scheduler stopped manually")    

```
# 6. Customization

You can customize the following aspects of the script:

1. Email content: Modify the send_email function in send_email.py to customize the email content.
2. Email scheduling: Adjust the scheduling parameters in main.py to change the frequency and timing of email reminders.
3. Criteria for sending reminders: Update the logic in main.py to define the conditions for sending email reminders based on the data.
