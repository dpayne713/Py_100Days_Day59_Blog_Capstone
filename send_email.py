import smtplib
import os

class SendEmail():
    def __init__(self):
        self.MY_EMAIL= os.environ["MY_EMAIL"]
        self.MY_PASSWORD= os.environ["MY_PASSWORD"]


    def send_form_email(self, form_data):

        data = {
            "name": form_data['name'],
            "email": form_data['email'],
            "phone": form_data['phone'],
            "message": form_data['message']

        }
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.MY_EMAIL, password=self.MY_PASSWORD)
            connection.sendmail(from_addr=self.MY_EMAIL,
                                to_addrs=self.MY_EMAIL,
                                msg=f"Subject: Message from {data['name']}\n\n"
                                    f"The following came from the My Blog form: \n" 
                                    f"\tName : {data['name']}\n"
                                    f"\tReply to : {data['email']}\n"
                                    f"\tPhone : {data['phone']}\n"
                                    f"\tMessage : {data['message']}")

