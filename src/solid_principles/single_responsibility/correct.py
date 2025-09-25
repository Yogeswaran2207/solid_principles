class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)
        self.send_notification(user)

    def send_notification(self, user):
        print(f"Notification: User {user} has been added.")

# Example usage
if __name__ == "__main__":
    manager = UserManager()
    manager.add_user("Alice")