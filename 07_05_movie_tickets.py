while True:
    age = input("Please enter your age (or 'quit' to exit):")
    if age.lower() == 'quit':
        break

    age = int(age)

    if age < 3:
        price = 0
    
    elif 3 <= age <= 12:
        price = 10

    else:
        price = 15

    print(f"\nThe cost of your movie ticket is: ${price}")