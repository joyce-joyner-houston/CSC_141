class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def describe_user(self):
        print(f"User: {self.first_name}, {self.last_name}")
        print(f"Age: {self.age}")


    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back!")


#Instances of Users
user_1 = User("Hanna", "Smith", 23)
user_2 = User("Alex", "Jackson", 14)
user_3 = User("Harry", "Johnson", 67)


#Methods for all Users
user_1.describe_user
user_1.greet_user

user_2.describe_user
user_2.greet_user

user_3.describe_user
user_3.greet_user