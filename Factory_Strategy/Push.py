from Factory_Strategy.Notification import Notification


class Push(Notification):

    @staticmethod
    def send(mess: str = None) -> None:
        print(f"notify via Push: {mess}".title())
