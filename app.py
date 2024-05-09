
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import schedule
import time
from datetime import datetime
from checks import Checks
       
def send_email(message):
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M")
    # Email configuration
    email_sender = 'miriamsh888@gmail.com'
    email_receiver = 'miriamsh888@gmail.com'
    password = os.environ.get('EMAIL_PASSWORD')

    # Create message
    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg['Subject'] = f'Live Tracker Report {formatted_datetime}'
    msg.attach(MIMEText(message, 'plain'))

    # Send email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_sender, password)
        smtp.send_message(msg)


def run_script():
    run_check = Checks()
    pegaus_status=run_check.check_pegasus()
    eventhub_status=run_check.check_eventhub()
    resume_status=run_check.check_resume()
    
    message = f'Pegasus: {pegaus_status}\n' \
          f'Eventhub: {eventhub_status}\n' \
          f'Resume: {resume_status}\n\n' \
          f'Have A Great Day!'
    
    send_email(message)
    print(message)
    return 


schedule.every().day.at("08:00").do(run_script)  # First run at 8 AM
schedule.every().day.at("20:00").do(run_script)  # Second run at 8 PM


def main():
    while True:
        schedule.run_pending()
        time.sleep(10800)  # Sleep for 3 hours (10800 seconds)

if __name__ == "__main__":
    main()

