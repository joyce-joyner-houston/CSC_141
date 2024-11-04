#Challenge level - 10
#restaurant.py
class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        print(f"{self.name} serves {self.cuisine_type} cuisine.")


    def open_restaurant(self):
        print(f"{self.name} is now open!")


#import_restaurant.py
from restaurant import Restaurant

my_restaurant = Restaurant("Good Eat's", "American")
my_restaurant.describe_restaurant()
