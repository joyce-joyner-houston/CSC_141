favorite_places = {'Greg': ['New York', 'Paris', 'Tokyo'],
    'Henry': ['Los Angeles', 'Miami, Austin'],
    'Charles': ['Chicago', 'Houston', 'Seattle']
}

for person, places in favorite_places.items():
    places_list = ','.join(places)

    print(f"{person}'s favorite places are: {places_list}\n")