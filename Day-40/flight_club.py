import smtplib
import requests

sheet_endpoint = 'https://api.sheety.co/a427deabbe2fc80f1332c178af08a3aa/fligh43Als/users'
MY_EMAIL = ''
MY_PASSWORD = ''

def join_club():
    print("Welcome to Guri's Flight Club\nWe find the best flight deals and email you.\n")
    first_name = input('What is your first name?\n')
    last_name = input('What is your last name?\n')
    email = input('What is your email?\n')
    verify = input('Type again your email.\n')
    if email == verify:
        sheet_params = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
            }
        }
        requests.post(url=f'{sheet_endpoint}', json=sheet_params)
        print('Success, your in the club!')
    else:
        print('Emails dont match. Please, type your information again.\n')
        join_club(),


def get_customer_emails():
    response = requests.get(sheet_endpoint)
    data = response.json()
    customer_data = data["users"]
    return customer_data


def send_emails(emails, message, link):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        for email in emails:
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=f"Subject:New Low Price Flight!\n\n{message}\n{link}".encode('utf-8')
            )
