#Challenge level - 5
class User:
    def __init__(self, username):
        self.usernamename = username
        self.login_attempts = 0


    def increment_login_attempts(self):
        self.login_attempts += 1


    def reset_login_attempts(self):
        self.login_attempts = 0


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
