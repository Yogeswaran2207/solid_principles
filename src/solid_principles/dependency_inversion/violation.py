class Database:
    def connect(self):
        return "Connecting to the database"

class UserService:
    def __init__(self):
        self.database = Database()  # High-level module depends on low-level module

    def get_user(self, user_id):
        connection = self.database.connect()
        return f"{connection}: Fetching user with ID {user_id}"


# Example usage
if __name__ == "__main__":
    user_service = UserService()
    print(user_service.get_user(1))