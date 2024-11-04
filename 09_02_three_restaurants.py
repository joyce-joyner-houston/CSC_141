class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")


    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")

restaurant = Restaurant("Good Eat's", "American")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

my_restaurant = Restaurant("Japan Village", "Japanese")
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

your_restaurant = Restaurant("Mama's Pizza", "Italian")
print(your_restaurant.restaurant_name)
print(your_restaurant.cuisine_type)
your_restaurant.describe_restaurant()
your_restaurant.open_restaurant()