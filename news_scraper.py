import requests     # http requests

from bs4 import BeautifulSoup # web Scraping 

# Send the mail
import smtplib 

#email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# System date and time manipulation
import datetime

now = datetime.datetime.now()


# email content placeholder
content = ''

# extracting Hacker News Stories 
def extract_news(url):
    print('Extracting Hacker News Stories...')
    cnt = ''
    cnt += ('<b>HN Top Stories:<br>' + '<br>' + '-'*50 + '<br>')
    # get the content of the url
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content,'html.parser')
    # extract cell of a table
    # we use enumarate because we want to have the result with numbers
    # if verifies that we take line except the last one with More
    for i,tag in enumerate(soup.find_all('td',attrs={'class':'title','valign':''})):
        cnt += ((str(i+1)+' :: ' + tag.text + "\n" + '<br>') if tag.text != 'More' else '')
    return (cnt)

cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('<br>------<br>')
content += ('<br><br>End of Message')

# Send the email
print('composing Email')

# update your email details
SERVER = 'smtp.gmail.com'   # your smtp server
PORT = 587  # your port number 
FROM = input('Enter your email')  # "your from email id"
TO = input('Enter recipient email')    # "your to email ids" # can be a list
PASS =  input('Enter password')  # "your email id's password"


# Create a text message
msg = MIMEMultipart()

# email subject
msg['Subject'] = 'Top News Stories HN [Automated Email]' + '' + str(now.day) + '-' + str(now.year)
msg['From'] = FROM
msg['To'] = TO

# email body
msg.attach(MIMEText(content, 'html'))

# Authenticate server
print('Initiating Server...')

server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(1)
server.ehlo()
#start secure connexion
server.starttls()

server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email Sent...')
server.quit()