while True:
    topping = input("Enter a pizza topping (or 'quit' to finish):")
    if topping.lower() == 'quit':
        break
    print(f"\nI'll add {topping} to your pizza!")
