#Challenge level - 1
try:
    num1 = input("Enter the first number: ")
    num1 = int(num1)

    num2 = input("Enter the second number: ")
    num2 = int(num2)

    result = num1 + num2
    print(f"The result of {num1} + {num2} is: {result}")


except ValueError:
    print("No valid number detected. Please enter numeric values.")