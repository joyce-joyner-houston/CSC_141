#Challenge level - 2
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")


#IcecreamStand class from Restaurant
class IcecreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []


    def add_flavors(self, flavors):
        self.flavors.extend(flavors)


    def display_flavors(self):
        print(f"{self.restaurant_name} offers:")
        for flavor in self.flavors:
            print(f"- {flavor}")


#Instances for IcecreamStand
ice_cream_stand = IcecreamStand("Scream for Ice Cream", "Dessert")
ice_cream_stand.add_flavors("Vanilla", "Chocolate", "Strawberry", "Cookie Dough", "Birthday Cake")
ice_cream_stand.display_flavors()
