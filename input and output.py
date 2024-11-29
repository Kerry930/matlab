# Simple Calculator Program

def calculator():
    print("Welcome to the Simple Calculator!")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Taking user input for the operation
    choice = input("Enter choice (1/2/3/4): ")

    # Checking if the input choice is valid
    if choice in ['1', '2', '3', '4']:
        # Taking user input for numbers
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Performing calculations based on the choice
        if choice == '1':
            print(f"The result of {num1} + {num2} is {num1 + num2}")
        elif choice == '2':
            print(f"The result of {num1} - {num2} is {num1 - num2}")
        elif choice == '3':
            print(f"The result of {num1} * {num2} is {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"The result of {num1} / {num2} is {num1 / num2}")
            else:
                print("Error: Division by zero is undefined.")
    else:
        print("Invalid input! Please select a valid operation.")

# Run the calculator function
calculator()
