pet_1 = {
    'owner': 'Alice',
    'kind': 'Dog',
    'name': 'Rex'
}

pet_2 = {
    'owner': 'Bob',
    'kind': 'Cat',
    'name': 'Whiskers'
}

pet_3 = {
    'owner': 'Charlie',
    'kind': 'Parrot',
    'name': 'Polly'
}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"Owner: {pet['owner']},
          Kind: {pet['kind']}, 
          Name: {pet['name']}\n")