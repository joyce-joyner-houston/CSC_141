pet_1 = {
    'owner': 'Alice',
    'kind': 'Dog',
    'name': 'Rex',
    'age': 5
}

pet_2 = {
    'owner': 'Bob',
    'kind': 'Cat',
    'name': 'Whiskers',
    'age': 1
}

pet_3 = {
    'owner': 'Charlie',
    'kind': 'Parrot',
    'name': 'Polly',
    'age': 3
}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"Owner: {pet['owner']}")
    print(f"  Kind: {pet['kind']}")
    print(f"  Name: {pet['name']}")
    print(f"  Age: {pet['age']} years\n")