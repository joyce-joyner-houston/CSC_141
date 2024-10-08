#Exercise 7-4, active variable
topping_count = 0
max_topping = 6

while True:
    topping = input("Enter a pizza topping (or 'quit' to finish):")
    if topping.lower() == 'quit':
        break
    print(f"\nI'll add {topping} to your pizza!")
    topping_count += 1