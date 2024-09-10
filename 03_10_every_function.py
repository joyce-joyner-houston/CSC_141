cities = ['New York', 'Chicago', 'Miami', 'New Orleans', 'Honolulu', 'Ocean City']
message = f"Welcome to {cities[0].title()}"
print(message)

message = f"Welcome to {cities[1].title()}"
print(message)

message = f"Welcome to {cities[2].title()}"
print(message)

message = f"Welcome to {cities[3].title()}"
print(message)

message = f"Welcome to {cities[4].title()}"
print(message)

message = f"Welcome to {cities[5].title()}"
print(message)

cities = ['New York', 'Chicago', 'Miami', 'New Orleans', 'Honolulu', 'Ocean City']
cities.remove('New York')
print(cities)

cities.insert(0, 'Detroit')
cities.insert(2, 'Cincinnati')
cities.append('Baltimore')

cities = ['New York', 'Chicago', 'Miami', 'New Orleans', 'Honolulu', 'Ocean City']
popped_cities = cities.pop
print(popped_cities)

cities = ['New York', 'Chicago', 'Miami', 'New Orleans', 'Honolulu', 'Ocean City']
cities.sort()
print(cities)

cities = ['New York', 'Chicago', 'Miami', 'New Orleans', 'Honolulu', 'Ocean City']
cities.reverse()
print(cities)

cities = ['New York', 'Chicago', 'Miami', 'New Orleans', 'Honolulu', 'Ocean City']
number_cities = len(cities)
print(number_cities)