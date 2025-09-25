class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)
        self.send_notification(user)

    def send_notification(self, user):
        print(f"Notification: User {user} has been added.")

    def get_users(self):
        return self.users


# Example usage
if __name__ == "__main__":
    user_manager = UserManager()
    user_manager.add_user("Alice")
    user_manager.add_user("Bob")
    print(user_manager.get_users())