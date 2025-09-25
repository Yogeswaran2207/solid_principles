class NotificationService:
    def send_notification(self, message):
        print(f"Sending notification: {message}")


class UserService:
    def __init__(self, notification_service):
        self.notification_service = notification_service

    def create_user(self, username):
        # Logic to create a user
        print(f"User {username} created.")
        self.notification_service.send_notification(f"Welcome {username}!")


# Usage
if __name__ == "__main__":
    notification_service = NotificationService()
    user_service = UserService(notification_service)
    user_service.create_user("Alice")