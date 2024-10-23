#sandwiches.py
def make_sandwich(*items):
    print("What would you like on your sandwich?")
    for item in items:
        print(f"- {item}")


#user_porfile.py
def build_profile(first, last, **user_info):
    profile = {
        'first_name' = first,
        'last_name' = last
        }
    
    profile.update(user_info)
    return profile


#cars.py
def make_car(manufacturer, model, **car_info):
    car = {
        'manufacturer' = manufacturer,
    'model' = model,
    }

    car.update(car_info)
    return car