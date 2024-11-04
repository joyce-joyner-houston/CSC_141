class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size


    def get_range(self):
        if self.battery_size == 65:
            return 190 #190 miles with 65 kwh battery
        return 140 #140 miles with 75 kwh battery
    

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65
            print("Battery upgraded to 65 kwh.")

#electric_car.py
class ElectricCar:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.battery = Battery()


my_electric_car = ElectricCar('Jeep', 'Wrangler 4xe', 2024)

print(f"Initial range: {my_electric_car.battery.get_range()} miles")
my_electric_car.battery.upgrade_battery()
print(f"Range after upgrade: {my_electric_car.battery.get_range()} miles")
