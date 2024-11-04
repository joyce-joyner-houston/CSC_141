#Challenge level - 10
#user_module.py
class User:
    def __init__(self, username):
        self.usernamename = username
        self.login_attempts = 0


    def increment_login_attempts(self):
        self.login_attempts += 1


    def reset_login_attempts(self):
        self.login_attempts = 0


from user_module import User

class Privileges:
    def __init__(self):
        # Define the privileges list here
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user"
        ]

    def show_privileges(self):
        print("Administrator Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    def __init__(self, username):
        super().__init__(username)
        self.privileges = Privileges()


from admin_module import Admin

admin_user = Admin("admin_user")
admin_user.privileges.show_privileges()
