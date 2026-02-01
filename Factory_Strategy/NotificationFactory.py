from Factory_Strategy.Notification import Notification
from Factory_Strategy.NotificationTypes import NotificationTypes
from Factory_Strategy import Email, Push, Sms
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
            return cls._registy[notify_type]
        else:
            raise ValueError(
                f"Oops! {notify_type} is not a valid notification type."
                )
