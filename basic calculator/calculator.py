print("Welcome to Calculator Project")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Square")
print("7. Power")
print("8. Exit\n")

while True:
    try:
        option = int(input("Select an option for the Basic Calculator Project: "))
        
        if option == 1:
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
            print("Addition:", num1 + num2, "\n")
        
        elif option == 2:
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
            print("Subtraction:", num1 - num2, "\n")
        
        elif option == 3:
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
            print("Multiplication:", num1 * num2, "\n")
        
        elif option == 4:
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
            if num2 != 0:
                print("Division:", num1 / num2, "\n")
            else:
                print("Error! Division by zero.\n")
        
        elif option == 5:
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
            print("Modulus:", num1 % num2, "\n")
        
        elif option == 6:
            num = float(input("Enter the Number: "))
            print("Square:", num ** 2, "\n")
        
        elif option == 7:
            base = float(input("Enter the Base Number: "))
            exponent = float(input("Enter the Exponent: "))
            print("Power:", base ** exponent, "\n")
        
        elif option == 8:
            print("Exiting the Calculator. Goodbye!")
            break
        
        else:
            print("Invalid Choice! Please select a valid option.\n")
    
    except ValueError:
        print("Invalid input! Please enter a valid number.\n")
