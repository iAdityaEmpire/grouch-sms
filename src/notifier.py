from pynotifier import Notification
import time, pathlib
import os
from twilio.rest import Client


account_sid = os.environ["TWILIO_SID"]
auth_token = os.environ["TWILIO_AUTH"]
client = Client(account_sid, auth_token)


def __always_true():
    return True

class Notifier:
    def __always_true():
        return True

    def __init__(self, title: str, info: str, state = __always_true):
        self.title, self.info = title, info
        self.status_check = state

    def send(self):
        dir = pathlib.Path(__file__).parent.absolute().as_posix() + '/grouch.ico'
        Notification(
            title=self.title,
            description=self.info,
            icon_path=dir,
            duration=7,
            urgency=Notification.URGENCY_CRITICAL
        ).send()
        message = client.messages.create(
                              body=self.title + "\n" + self.info,
                              from_='+19517244225',
                              to='+16095788255'
                          )
        message = client.messages.create(
                              body=self.title + "\n" + self.info,
                              from_='+19517244225',
                              to='+18569043341'
                          )
        time.sleep(7)

    def run(self):
        while not self.status_check():
            continue
        self.send()

    def run_async(self):
        if self.status_check():
            self.send()

    def run_force(self):
        self.send()
