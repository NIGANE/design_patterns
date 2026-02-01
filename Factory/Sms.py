from Factory.Notification import Notification


class Sms(Notification):

    @staticmethod
    def send(mess: str = None) -> None:
        print(f"notify via Sms: {mess}".title())
