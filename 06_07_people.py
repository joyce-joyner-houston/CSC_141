person_1 = {'first_name': 'Kayln', 'last_name': 'Peters'
          , 'age': '18', 'city': 'Bowie'}


person_2 = {'first_name': 'Bob', 'last_name': 'Johnson'
          , 'age': '43', 'city': 'Chicago'}


person_3 = {'first_name': 'Jack', 'last_name': 'Stuber'
          , 'age': '29', 'city': 'Salt Lake City'}


people = [person_1, person_2, person_3]

for person in people:
    print(f"{person['first_name']} {person['last_name']}, 
          Age: {person['age']},
          City:{person['city']}\n")