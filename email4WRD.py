import pandas as pd
import smtplib
import threading
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pythonhtmltext import getHTML

def sendEmail(message, company_name, email):
    print(email)
    # TO = 'tyree@equal.vc'
    # SUBJECT = 'You Are Invited To Attend 4WRD Ventures Pitch Competition'
    # TEXT = ''
    # message = message[0]
    # # Gmail Sign In
        # Create message container - the correct MIME type is multipart/alternative here!
    try:
        FROM = 'ali@4wrdventurecapital.com'
        TO = email
        MESSAGE = MIMEMultipart('alternative')
        MESSAGE['subject'] = company_name + ' Is Invited To Attend 4WRD Ventures Pitch Competition'
        MESSAGE['To'] = TO
        MESSAGE['From'] = FROM
        MESSAGE.preamble = """
        Your mail reader does not support the report format.
        Please visit us <a href="http://www.mysite.com">online</a>!"""

        HTML_BODY = MIMEText(message[0], 'html')

        MESSAGE.attach(HTML_BODY)
        password = 'xfoqquqfefntmqsx'
        server = smtplib.SMTP('smtp.gmail.com')
        server.starttls()
        server.login(FROM,password)
        server.sendmail(FROM, [TO], MESSAGE.as_string())
        server.quit()
    except Exception as e:
        print(e)

def massEmail(dataframe):
    # print(dataframe.head())
    # print(len(message))
    for index, row in dataframe.iterrows():
        print(row['company_name'], row['email'])
        message = [getHTML(row['company_name'])]#, row['company_name']]
        # timer = threading.Timer(2.0, sendEmail, args=message)
        # timer.start()
        sendEmail(message, row['company_name'], row['email'])

if __name__ == '__main__':
    dataframe = pd.read_csv('../../Downloads/my300New27.csv')
    massEmail(dataframe)
