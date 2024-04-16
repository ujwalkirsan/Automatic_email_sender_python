# 1. How to send automated email remainder to students

This is a Python script for automating the sending of email reminders based on data from a Google Sheets document. It uses the pandas library to read data from the Google Sheets document, and the apscheduler library to schedule and execute email sending tasks periodically.

# 2. Prerequisites

Before running the script, ensure you have the following installed:

Python 3.x
Required Python packages (pandas, apscheduler)
An email account (e.g., Gmail, Outlook) for sending emails
Access to a Google Sheets document with the required data

# 4. Setup

1. navigate the project directory:
`cd automated-email-reminder`

2. Install the required Python packages:
`pip install -r requirements.txt`

3. Set up environments variables:
Create a '.env' file in the project directory with the following variables:
ex:-
EMAIL=your_email@example.com
PASSWORD=your_email_password
Replace your_email@example.com and your_email_password
with your email credentials.

NOTE :- If you are using gmail.com as your email server then make a new app-specific password in app passwords in google accounts and then give any name to it and then it will show you a 16 digit alphabets password then you have to paste this password as the email password in your env file
(for the above method you need to verify that your two factor authentication of the google is on otherwise the app password will not show you)
link to app password :- https://accounts.google.com/v3/signin/challenge/pwd?TL=AEzbmxx-_vJrRHvDX_9gJcYIOdjDSNqm_ouMGFF-V_ZqNSNm82s-dK3opeU2dOJk&cid=2&continue=https%3A%2F%2Fmyaccount.google.com%2Fapppasswords&flowName=GlifWebSignIn&followup=https%3A%2F%2Fmyaccount.google.com%2Fapppasswords&ifkv=ARZ0qKLF45IQWgmvdZt3EQ-xIAEwO0Pr58My2H5tl3zfqL7fRLVal-salXWYanmi2RvEBFA3L-NNGg&osid=1&rart=ANgoxcdi_d-pr6T3OiSThx18wxtz0y3EkcU2niNlA2hQBhoBr_KcxWhAmukCIB8bmgDVI1l_B96gm2vYehgu2SIIOPIqW_6_Grf-bo6zfWXDzKtE1c73bwE&rpbg=1&service=accountsettings&theme=mn