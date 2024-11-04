#Challenge level - 8
class User:
    def __init__(self, username):
        self.username = username
        self.login_attempts = 0


    def increment_login_attempts(self):
        self.login_attempts += 1


    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges:
    def privileges(self, add, delete, ban):
        self.add = add
        self.delete = delete
        self.ban = ban


    def show_privileges(self):
        print("Administrator Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    def __init__(self, username):
        super().__init__(username)
        self.privileges = Privileges()


#Instance of User
user = User("hanna_smith")


#Increments for Login Attempts
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

print("Login attempts:", user.login_attempts)

user.reset_login_attempts()

print("Login attempts after reset:", user.login_attempts)


#Instance of Admin
admin_user = Admin("admin_user")
admin_user.privileges.show_privileges()
