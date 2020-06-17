#! python3
# emailer.py - Sends simple email to the receiver
# version 1.0
import re
import sys
from smtplib import SMTP_SSL
import ssl


def checkEmail(email: str) -> bool:
    return len(re.compile(
        r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)').search(email).groups()) == 1


def emailer() -> None:
    receiver_email = str(input("Please enter the receiver's email: "))
    is_valid_email = checkEmail(receiver_email)
    if is_valid_email:
        # TODO enable entering email subject
        # subject = str(input("Please enter email subject: "))
        body = str(input("Please enter email body: "))
        if len(body) == 0:
            print("Please enter a valid body text")
            sys.exit()
        else:
            ask_to_send = str(
                input(f"Send the email to {receiver_email}? <y|n>"))
            if ask_to_send == 'y' or ask_to_send == 'Y':
                password = str(input("Enter email password: "))
                context = ssl.create_default_context()
                with SMTP_SSL("smtp.gmail.com", 567, context=context) as server:
                    server.login("dimashin9@gmail.com", password)
                    server.sendmail("dimashin9@gmail.com",
                                    "dshin19@myseneca.ca", body)
                pass
            else:
                print("Thank you for using email service")
                sys.exit()
    else:
        print("Email is not valid")
        sys.exit()


if __name__ == '__main__':
    emailer()
