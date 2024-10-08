vacation_poll = {}

while True:
    name = input("What is your name? (or 'quit' to exit):")
    if name.lower() == 'quit':
        break
    location = input("If you could visit one place in the world, where would you go?")
    vacation_poll[name] = location
    print(f"Thanks, {name}! Your dream vacation to location has been recorded.\n")


print("\nPoll Results:")
for name, location in vacation_poll.items():
    print(f"{name} would like to visit {location}.")