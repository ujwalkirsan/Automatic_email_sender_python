

import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path

from dotenv import load_dotenv


PORT = 587
# I am currently using outlook so i have used outlook email server we can also use gmail or yahoo
EMAIL_SERVER = "smtp-mail.outlook.com"
# EMAIL_SERVER = "smtp.gmail.com"  # if you are using google then use this and comment upper email_server
# Load environment variables
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)

# Read environment variables
sender_email = os.getenv("EMAIL")   # in case your env file not working then write your email and Password directly
password_email = os.getenv("PASSWORD")   # sender_email = "your_email@gmail.com" and password_email = "your_email_password" if you are using gmail server then use 16 digit alpha password as  I mentioned in the README file how to get the 16 digit password for your email account
def send_email(subject,receiver_email,name,percent,roll_no,classes,attachments=None):
    # create the base text message.
    msg = EmailMessage()
    msg["Subject"]=subject
    msg["From"]=formataddr(("DA213 Course IITG",f"{sender_email}"))
    msg["To"]=receiver_email
    msg["BCC"]=sender_email
    
    

    msg.set_content(
        f"""\
        Dear {name},
        We hope this email finds you well.
        We just wanted to drop you a quick note to remind you that out of 30 days you present only {classes} days in class and you have {percent}% of total 100% attendence .
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
        <p>We just wanted to drop you a quick note to remind you that out of 30 days of classes you present only in <strong> {classes} days </strong>  of class and you have  <strong>{percent}</strong> of total 100% attendence.</p>
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

    if attachments:
        for attachment in attachments:
            with open(attachment, "rb") as f:
                file_data = f.read()
                file_name = os.path.basename(attachment)
            msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)


    with smtplib.SMTP(EMAIL_SERVER,PORT) as server:
        server.starttls()
        server.login(sender_email,password_email)
        server.sendmail(sender_email,receiver_email,msg.as_string())
        print("Mail Send Successfully!!!!")

   # this is text case you change it and add your another email id to get the mail at account     
if __name__ == "__main__":
    send_email(
        subject = "Attendance Remainder: 220150026",
        name = "Ujwal Kirsan",
        receiver_email="ujwalkirsan2003@gmail.com", 
        percent="40%",
        roll_no="220150026",
        classes="12",
        attachments=["requirements.txt","IITG_logo.png"]
        
        )        
