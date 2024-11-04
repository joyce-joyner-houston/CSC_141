
#Challenge level - 5
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")


    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")

    
    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment

restaurant = Restaurant("Good Eat's", "American")


print("Number of customers served:", restaurant.number_served)

restaurant.set_number_served(30)
print("Number of customers served after work day:", restaurant.number_served)

restaurant.increment_number_served(10)
print("Number of customers served after increment:", restaurant.number_served)
