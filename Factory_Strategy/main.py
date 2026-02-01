from Factory_Strategy.NotificationTypes import NotificationTypes
from Factory_Strategy.NotificationFactory import NotificationFactory


def main() -> None:
    print("========== Factory (Notification) ==========")

    choices = {
        "1": NotificationTypes.EMAIL,
        "2": NotificationTypes.PUSH,
        "3": NotificationTypes.SMS
    }

    print("\nAvailable notification methods:")
    for key, n_type in choices.items():
        print(f"[{key}] {n_type.name}")

    selection = input(f"\nChoose a method {list(choices.keys())}: ")

    target_enum = choices.get(selection)

    if not target_enum:
        print("❌ Invalid selection! Please pick 1, 2, or 3.")
        return

    try:
        notif = NotificationFactory.get_notification(target_enum)

        notif.send("Mastery achieved! The factory is working.")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
