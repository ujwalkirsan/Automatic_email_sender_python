# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 10:56:42 2024

@author: ujwal
"""

#import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr


PORT = 587
# I am currently using gmail so i have used outlook email server we can also use outlook or yahoo
EMAIL_SERVER = "smtp.gmail.com"


# Read environment variables
sender_email = "shekharkirsan@gmail.com"
password_email = "xoahlxzgtfxwvucq"
def send_email(subject,receiver_email,name,percent,invoice_no,amount):
    # create the base text message.
    msg = EmailMessage()
    msg["Subject"]=subject
    msg["From"]=formataddr(("IIT Guwahati",f"{sender_email}"))
    msg["To"]=receiver_email
    msg["BCC"]=sender_email
    
    msg.set_content(
        f"""\
        Dear {name},
        We hope this email finds you well.
        We just wanted to drop you a quick note to remind you that out of 30 days you present only {amount} days in class and you have {percent}% of total 100% attendence .
        We would be really grateful if you could contact us and give us a reason for your absent and from now onwords you have to come to class daily.
        Otherwise you will have to face consequences
        Best regards,
        Team MinTech
        Proffessor
        IIT Guwahati
            """
        )
        # Add the html version.  This converts the message into a multipart/alternative
    # container, with the original text message as the first part and the new html
    # message as the second part.
    msg.add_alternative(
        f"""\
    <html>
      <body>
        <p>Dear {name},</p>
        <p>We hope this email finds you well.</p>
        <p>We just wanted to drop you a quick note to remind you that out of 30 days of classes you present only in <strong> {amount} days </strong>  of class and you have  <strong>{percent}</strong> of total 100% attendence.</p>
        <p>We would be really grateful if you could contact us and give us a reason for your absent and from now onwards you  have to come to class daily.</p>
        <p>Otherwise you will have to face consequences.</p>
        <p>Best regards,</p>
        <p>Team MinTech</p>
        <p>Proffessor</p>
        <p>IIT Guwahati</p>
      </body>
    </html>
    """,
        subtype="html",
    )
        
    with smtplib.SMTP(EMAIL_SERVER,PORT) as server:
        server.starttls()
        server.login(sender_email,password_email)
        server.sendmail(sender_email,receiver_email,msg.as_string())
        print("Mail Send Successfully!!!!")
        
if __name__ == "__main__":
    send_email(
        subject = "Attendance Remainder: 220150026",
        name = "Ujwal Kirsan",
        receiver_email="ujwalkirsan2003@gmail.com",
        percent="90%",
        invoice_no="220150026",
        amount="27",
        
        )        
