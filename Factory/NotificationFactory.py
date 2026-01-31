from Factory.Notification import Notification
from Factory.NotificationTypes import NotificationTypes
from Factory import Email, Push, Sms
from typing import Optional


class NotificationFactory:
    _registy = {
        NotificationTypes.EMAIL: Email,
        NotificationTypes.PUSH: Push,
        NotificationTypes.SMS: Sms
    }

    @classmethod
    def get_notification(
        cls, notify_type: str, mess: str = None
            ) -> Optional[Notification]:

        if notify_type in cls._registy:
            return cls._registy[notify_type].send()
        else:
            raise ValueError(
                f"Oops! {notify_type} is not a valid notification type."
                )
