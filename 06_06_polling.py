favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

people_in_poll = ['Jen', 'Sarah', 'Edward', 'Phil', 'Bob', 'Eve']

for person in people_in_poll:
    if person in favorite_languages:
        print(f"Thank you, {person}, for responding.")

    else:
        print(f"{person}, please take our favorite languages poll!")