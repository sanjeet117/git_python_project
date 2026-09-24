class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_user(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")

    def update_email(self, new_email):
        self.email = new_email