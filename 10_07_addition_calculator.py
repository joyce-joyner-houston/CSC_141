#Challenge level - 1
while True:

    try:
        num1 = input("Enter the first number: ")
        num1 = int(num1)

        num2 = input("Enter the second number: ")
        num2 = int(num2)

        result = num1 + num2
        print(f"The result of {num1} + {num2} is: {result}")
        break


    except ValueError:
        print("No valid number detected. Please enter numeric values.")