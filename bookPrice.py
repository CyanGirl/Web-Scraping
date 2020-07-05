import requests
from bs4 import BeautifulSoup
import smtplib


def check():
    # url for the page we want to scrape
    URL = 'https://www.amazon.in/Norwegian-Wood-Haruki-Murakami/dp/0099448823/ref=sr_1_1?dchild=1&keywords=murakami&qid=1593880305&sr=8-1'

    # we need to set the headr to give our browser info
    headers = {
        "User-Agent": 'can-be-get-from-google'}

    # Now we can get all the data from the page
    page = requests.get(URL, headers=headers)

    # to visualise everything in frm of HTMl, we need parser
    soup = BeautifulSoup(page.content, 'html.parser')

    # topull info
    title = soup.find(id="productTitle").get_text().strip()
    print(title)  # prints the entire division

    price = soup.find(id="soldByThirdParty").get_text().strip()
    price = float(price[2:5])
    print(price)

    if(price < 550):
        send_mail()


def send_mail():

    # setup sevrer
    server = smtplib.SMTP('smtp.gmail.com')
    server.ehlo()  # for establishing connection
    server.starttls()  # for encryption
    server.ehlo()

    server.login('sendermail', 'password')

    subject = 'Fall in Book Price!'
    body = 'Check the Book in the Amazon! Here is your discount. You can also access it through :\n\n https://www.amazon.in/Norwegian-Wood-Haruki-Murakami/dp/0099448823/ref=sr_1_1?dchild=1&keywords=murakami&qid=1593880305&sr=8-1 \n\nHave a great day!'

    msg = f"Subject: {subject}\n\n\n{body}"

    server.sendmail('sendermail', 'recievermail', msg)
    print("Mail has been sent!")

    server.quit()


check()
