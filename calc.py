while True:

    print("This is a simple calculator for performing basic arithmetic operations.")
    
    try:
            x = float(input("Please enter the first number: "))    # obtaining the inputs from the user
            y = float(input("Please enter the second number: "))
    except ValueError:   # checking for numerical values
        print("Invalid input. Please enter numeric values only.")
        continue

    q = input(
        "Which operation would you like to perform?"
        "(Add, Subtract, Multiply, Divide OR +, -, *, /): "
        ).lower()  #obtaining the operation

    if q == "add" or q == "addition" or q == "+": #handling cases for addition
        rs = x + y
        print ("The sum of {} and {} is: {}".format(x, y, rs))

    elif q == "subtract" or q == "subtraction" or q == "-": #handling cases for subtraction
        rs = x - y
        print ("The difference between {} and {} is: {}".format(x, y, rs))

    elif q == "multiply" or q == "multiplication" or q == "*": #handling cases for multiplication
        rs = x * y
        print ("The product of {} and {} is: {}".format(x, y, rs))  

    elif q == "divide" or q == "division" or q == "/": #handling cases for division
     if y == 0:   #checking for division by zero
        print("Error: Division by zero is not allowed.")
     else:
        rs = x / y
        print ("The quotient of {} divided by {} is: {}".format(x, y, rs))

    again = input("would you like to perform another calculation? (yes/no): ") #asking user if they want to perform another calculation
    if again.lower() != "yes":
        print("Thank you for using the calculator. Goodbye!")
        break



