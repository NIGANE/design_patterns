from Factory.Notification import Notification


class Email(Notification):

    @staticmethod
    def send(mess: str = None) -> None:
        print(f"notify via Email: {mess}".title())
